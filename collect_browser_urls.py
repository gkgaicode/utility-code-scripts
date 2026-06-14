import time
import os
import sys
import ctypes
import re
from datetime import datetime

# # ZenTab URL Collector Dependencies
# pyautogui
# pyperclip
# keyboard
# pygetwindow

# # Verify and import required external libraries
try:
    import pyautogui
    import pyperclip
    import pygetwindow as gw
except ImportError:
    print("=" * 60)
    print("Error: Missing required packages.")
    print("Please install them using:")
    print("  pip install pyautogui pyperclip pygetwindow")
    print("=" * 60)
    sys.exit(1)

def sanitize_filename(name):
    """
    Sanitizes a string to make it a safe filename on Windows.
    Replaces spaces, punctuation, and special symbols (like #, :, ,, etc.) with underscores,
    collapses multiple consecutive underscores into a single underscore,
    and strips leading/trailing underscores and dashes.
    """
    # Replace non-alphanumeric characters (except hyphens and periods) with underscores
    sanitized = re.sub(r'[^a-zA-Z0-9\-.]', '_', name)
    # Collapse multiple underscores
    sanitized = re.sub(r'_+', '_', sanitized)
    # Strip leading/trailing underscores and dashes
    return sanitized.strip('_').strip('-')


def safe_paste(retries=5, delay=0.05):
    """
    Safely reads from the clipboard, retrying if the clipboard is locked or busy.
    """
    for i in range(retries):
        try:
            return pyperclip.paste()
        except Exception:
            time.sleep(delay)
    return ""

def safe_copy(text, retries=5, delay=0.05):
    """
    Safely writes to the clipboard, retrying if the clipboard is locked or busy.
    """
    for i in range(retries):
        try:
            pyperclip.copy(text)
            return True
        except Exception:
            time.sleep(delay)
    return False

def force_focus_window(win):
    """
    Brings a window to the foreground robustly.
    Uses Win32 API calls via ctypes to restore minimized windows and set foreground focus.
    """
    hwnd = win._hWnd
    
    # 1. Simulate a keypress (Alt) to bypass Windows foreground-lock timeout
    pyautogui.press('alt')
    time.sleep(0.1)

    # 2. If minimized, restore the window
    if win.isMinimized:
        # SW_RESTORE = 9
        ctypes.windll.user32.ShowWindow(hwnd, 9)
        time.sleep(0.3)
    
    # 3. Bring to foreground
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    time.sleep(0.4)

def clean_webpage_title(window_title):
    """
    Removes common browser name suffixes to return a clean webpage title.
    """
    suffixes = [
        " - Google Chrome", " - Chrome",
        " - Microsoft Edge", " - Edge",
        " - Brave", " - Mozilla Firefox", " - DuckDuckGo"
    ]
    cleaned = window_title
    for suffix in suffixes:
        if cleaned.endswith(suffix):
            cleaned = cleaned[:-len(suffix)]
            break
        # Case insensitive secondary replacement
        if suffix.lower() in cleaned.lower():
            idx = cleaned.lower().rfind(suffix.lower())
            if idx != -1:
                cleaned = cleaned[:idx]
    return cleaned.strip()

def get_active_tab_url():
    """
    Uses pyautogui to select the address bar (Ctrl+L) and copy the URL (Ctrl+C).
    Returns the copied URL or None if not a valid link.
    Note: Clipboard backup and restore are handled once globally at the script level.
    """
    safe_copy("")  # clear clipboard to detect new copy
    
    # Highlight address bar
    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.15)
    
    # Copy URL
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.15)
    
    url = safe_paste().strip()
    
    if url.startswith("http://") or url.startswith("https://") or url.startswith("www."):
        return url
    return None

def select_browser_window():
    """
    Prompts the user to choose a browser and matches it to running windows.
    If multiple windows are found, lets the user select one.
    """
    print("\nSupported Browsers:")
    print("1) Google Chrome")
    print("2) Microsoft Edge")
    print("3) Mozilla Firefox")
    print("4) Brave")
    print("5) DuckDuckGo Browser")
    
    choice = input("\nSelect browser (1-5): ").strip()
    
    browser_mapping = {
        "1": ("Google Chrome", ["chrome", "google chrome"]),
        "2": ("Microsoft Edge", ["edge", "microsoft edge"]),
        "3": ("Mozilla Firefox", ["firefox", "mozilla firefox"]),
        "4": ("Brave", ["brave"]),
        "5": ("DuckDuckGo", ["duckduckgo"])
    }
    
    if choice not in browser_mapping:
        print("Invalid browser selection.")
        return None, None
        
    display_name, search_terms = browser_mapping[choice]
    
    # Search all windows
    all_windows = gw.getAllWindows()
    matching_windows = []
    
    for win in all_windows:
        if win.title:
            title_lower = win.title.lower()
            if any(term in title_lower for term in search_terms):
                matching_windows.append(win)
                
    if not matching_windows:
        print(f"\nNo running windows found for browser: {display_name}")
        print("Make sure the browser is open and running.")
        return None, None
        
    # Handle multiple windows
    if len(matching_windows) > 1:
        print(f"\nMultiple windows found for {display_name}:")
        for idx, win in enumerate(matching_windows):
            print(f"  {idx + 1}) {win.title}")
        try:
            sel = input(f"Select window (1-{len(matching_windows)}) [default 1]: ").strip()
            sel_idx = int(sel) - 1 if sel else 0
            if sel_idx < 0 or sel_idx >= len(matching_windows):
                sel_idx = 0
            return matching_windows[sel_idx], display_name
        except ValueError:
            return matching_windows[0], display_name
            
    return matching_windows[0], display_name


def save_and_export_tabs(collected_tabs, browser_name=None):
    """
    Writes tabs to notes file and handles copy-to-clipboard options.
    Filters out duplicate URLs to keep the saved and copied list unique.
    """
    if not collected_tabs:
        print("No tabs collected.")
        return
        
    seen_urls = set()
    unique_tabs = []
    duplicate_count = 0
    
    for url, title in collected_tabs:
        # Normalize URL to avoid duplicates with trailing slashes or case differences in domain
        try:
            # Handle standard normalization (lowercase domain, strip trailing slash)
            if "://" in url:
                parts = url.split("://", 1)
                protocol = parts[0]
                rest = parts[1]
                if "/" in rest:
                    domain, path = rest.split("/", 1)
                    norm_url = f"{protocol}://{domain.lower()}/{path.rstrip('/')}"
                else:
                    norm_url = f"{protocol}://{rest.lower()}".rstrip('/')
            else:
                norm_url = url.lower().rstrip('/')
        except Exception:
            norm_url = url.rstrip('/')

        if norm_url not in seen_urls:
            seen_urls.add(norm_url)
            unique_tabs.append((url, title))
        else:
            duplicate_count += 1
            
    if not unique_tabs:
        print("No unique tabs collected.")
        return
        
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # 1. Format Markdown Output
    md_output = f"## Browser Session - {timestamp}\n"
    for title, url in unique_tabs:
        md_output += f"- [{title}]({url})\n"
    md_output += "\n"
    
    # 2. Write to File
    # Prefix the filename with the selected browser name if available
    prefix = ""
    if browser_name:
        prefix = browser_name.lower().replace(" ", "_") + "_"
    
    # Human-readable date and time stamp default: e.g. "google_chrome_tabs_2026-05-23_15-21-47.txt"
    default_filename = f"{prefix}tabs_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    print(f"\nEnter a name for your note file.")
    user_file = input(f"File Name [default: {default_filename}]: ").strip()
    
    if user_file:
        file_name = sanitize_filename(user_file)
        # Ensure it has a file extension
        if not file_name.endswith('.txt') and not file_name.endswith('.md'):
            file_name += '.txt'
    else:
        file_name = default_filename
        
    file_exists = os.path.exists(file_name)
    with open(file_name, "a", encoding="utf-8") as f:
        if not file_exists:
            f.write("# Collected Browser URLs & Notes\n\n")
        f.write(md_output)
    
    duplicates_msg = f" (Filtered {duplicate_count} duplicate URLs)" if duplicate_count > 0 else ""
    print(f"\n[Success] Saved {len(unique_tabs)} unique tabs to: {os.path.abspath(file_name)}{duplicates_msg}")

    
    # 3. Interactive Clipboard Copy Option
    copy_choice = input("\nWould you like to copy the formatted content to your clipboard? (y/n) [default y]: ").strip().lower()
    if copy_choice != 'n':
        if safe_copy(md_output.strip()):
            print("[Clipboard] Copied formatted Markdown note successfully!")
        else:
            print("[Error] Failed to copy note to clipboard (clipboard was locked).")


def run_tab_iterator():
    """
    Main controller to target browser, loop tabs, and write findings.
    """
    print("=" * 60)
    print("             ZenTab Browser URL Collector")
    print("=" * 60)
    
    target_win, browser_name = select_browser_window()
    if not target_win:
        return
        
    print(f"\nSelected window: '{target_win.title}'")
    print("--> Preparing to focus window and start scanning...")
    print("--> Please do NOT use keyboard/mouse until completion (takes ~5-15s)")
    time.sleep(1.5)
    
    # Backup user's original clipboard content ONCE
    old_clipboard = safe_paste()
    collected_tabs = []
    
    try:
        # Focus the window
        force_focus_window(target_win)
        
        # Jump to first tab (Ctrl+1)
        pyautogui.hotkey('ctrl', '1')
        time.sleep(0.5)
        
        # Retrieve current active window title and url for the 1st tab
        first_title = clean_webpage_title(target_win.title)
        first_url = get_active_tab_url()
        
        if not first_url:
            # Try a quick fallback retry in case key registration was delayed
            time.sleep(0.3)
            first_url = get_active_tab_url()
            
        if not first_url:
            print("\nError: Could not retrieve URL from the first tab.")
            print("Please ensure the browser is not in a modal state, setting menu, or empty page.")
            return
            
        first_tab_id = (first_url, first_title)
        collected_tabs.append(first_tab_id)
        
        print(f"\nScanning tabs:")
        print(f"  [Tab 1] {first_title} -> {first_url}")
        
        # Loop to capture remaining tabs
        # We cap at 100 tabs to prevent any potential infinite loops
        max_tabs = 100
        for idx in range(2, max_tabs + 1):
            # Move to next tab
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(0.35)
            
            # Get active window title and URL
            curr_title = clean_webpage_title(target_win.title)
            curr_url = get_active_tab_url()
            
            # If no URL, try a short retry
            if not curr_url:
                time.sleep(0.2)
                curr_url = get_active_tab_url()
                
            if not curr_url:
                # Skip empty tabs or browser internal tabs (like settings)
                print(f"  [Tab {idx}] skipped (unreadable URL or empty tab)")
                continue
                
            current_tab_id = (curr_url, curr_title)
            
            # Check loop condition: did we cycle back to the first tab?
            if current_tab_id == first_tab_id:
                print("\n--> Wrapped around back to the first tab.")
                break
                
            # Check stuck condition: if title/URL did not change from previous tab
            # (This happens if there is only 1 tab in the window, or Ctrl+Tab is blocked)
            if current_tab_id == collected_tabs[-1]:
                print("\n--> Checked all tabs (no further tab navigation detected).")
                break
                
            collected_tabs.append(current_tab_id)
            print(f"  [Tab {idx}] {curr_title} -> {curr_url}")
            
    except Exception as e:
        print(f"\nAn error occurred during tab scanning: {e}")
        print("Saving already collected tabs...")
        
    finally:
        # Restore user's original clipboard content ONCE
        safe_copy(old_clipboard)
        
        # Return focus to python console/terminal (best effort)
        try:
            pyautogui.hotkey('alt', 'tab')
        except:
            pass
            
        # Save whatever was collected (even if we crashed or were interrupted)
        if collected_tabs:
            save_and_export_tabs(collected_tabs, browser_name)
        else:
            print("No tabs were successfully collected.")

if __name__ == "__main__":
    try:
        run_tab_iterator()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
