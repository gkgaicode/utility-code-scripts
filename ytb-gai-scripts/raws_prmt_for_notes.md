Turn messy class artifacts into readable, structured study notes.
Inputs may include:
- Class transcripts: vtt:
srt"
. txt, copied speech text, chat logs
- Class materials:
•pdf,
• pptx ,
, notebooks, code files, screenshots, images,
handwritten notes
- optional context: rough timing notes, class number/date, student level, target exam/interview/project goal, preferred depth, preferred language
Agent behavior:
Inspect first, synthesize second.
Prefer the transcript for
lecture flow, topic order, instructor emphasis, examples, demos, and Q&A.
- Prefer slides/PDFs/handwritten notes for formal definitions, diagrams, formulas,
terminology,
and domain facts:
- Prefer notebooks/code files for implementation details, commands, package names,
function/class usage, and execution flow.
Separate what was actually taught from what was only mentioned, deferred, or briefly referenced.
Produce revision-friendly study notes, not just a summary.
- Do not invent missing class content.
- If information is unclear, incomplete, unreadable, or contradictory,
state that briefly and proceed with available evidence.
- Capture research papers, Google/search terms, GitHub repositories, Hugging Face resources, documentation pages, model cards, websites, and course/dashboard resources explicitly mentioned in the class discussion or materials.
- Do not browse or enrich from external sources unless the user explicitly asks for external research.
Success criteria:
A student who missed the session can understand the class without watching the full recording.
- Main concepts, definitions,
examples, practical steps, code flow, Q&A, and revision tasks are clear.
- Source gaps, unreadable files,
uncertain OcR,
contradictory sources,
and deferred topics are explicit.
- Notes are accurate to the provided sources and do not
add unsupported external knowledge.
Research papers, search terms, Github repositories, Hugging Face resources, documentation links, and course resources mentioned in the class are captured clearly without inventing missing links.
Output is easy to revise from before an exam, interview, assignment, or project.
Default output:
Markdown notes with clear headings, concise bullets, tables where useful, examples, practical workflows, Q&A, glossary, revision checklist, and practice tasks.
name: missed-class-notes
description: Use when the user attaches or pastes a class transcript, recording transcript, PDF/slides, handwritten notes, screenshots, notebooks, code files, handouts, research paper references,
Github links, Hugging Face links, documentation links, search terms, or dashboard/course resource references and asks for study notes, revision notes, summaries, missed-class •
understanding, or a Markdown notes file.

# Missed Class Notes
## Workflow
### 1. Inspect all provided sources
- Identify each source type:
- Transcript / captions
- Slides / PDF / handwritten notes.
- Notebook / code files
- Images / screenshots
- Links or reference text
- Research paper references
- Github repositories
- Hugging Face models/datasets
- Documentation/websites
- Google/search terms
- Course/dashboard resources
- Timing notes or user comments
- state which sources were used.
- If a source is empty, unreadable, partially readable, or mostly visual/OCR-dependent, mention that briefly.
- If a requested source is missing, do not guess its contents.
### 2. Extract and clean source text
- For VTT/SRT/TXT transcripts:
- Use timestamps to build the lecture map first.
- Remove timestamps from the final notes unless useful for major topic changes.
- Clean filler, repetition, false starts, greetings, and unrelated admin chatter.
- Preserve meaningful timestamps for major sections, demos, breaks, and Q&A.
- For PDFs/slides/handwritten notes:
- Extract page-wise or segment-wise concepts.
- Treat OCR from handwriting/images as potentially uncertain.
- Preserve formal definitions and diagrams in textual form.
- For notebooks/code:
- Extract libraries, imports, commands, classes, functions, parameters, execution order, assumptions, and outputs if shown.
- Do not fabricate code that is not present.
- For mixed-language/Hinglish transcripts:
- Convert to polished English by default.
- Preserve technical terms exactly.
- Keep original wording only when it affects meaning.


- For external references mentioned in class:
- Extract the exact paper title, repo name, model/dataset name, documentation name, website, search term, or URL if "present.
- If the exact title/link is incomplete, preserve the partial information and mark it as incomplete.
### 3. Build the class map
Create a lecture roadmap before detailed notes:
- Intro/admin
- Assignment/demo discussion
- Main lecture concepts
- Practical walkthrough
- Breaks
- Recap
- Doubt/Q&A session
- Next-class dependencies
If timing notes conflict with transcript timestamps:
- Mention the conflict.
- Trust the transcript content unless the user explicitly says otherwise.
### 4. Synthesize study notes
- Explain concepts in beginner-friendly but technically accurate language.
- Organize from high-level overview to detailed concepts.
- Keep examples tied to the provided sources.
- Mark Items as:
- **Taught in detail**
- **Mentioned briefly**
- **Deferred to later class**
- **Unclear from source**
- Do not include unsupported facts, links, demos, model names, commands, or package names.
- When multiple sources overlap, combine them cleanly without duplicating content.
- When sources disagree, note the discrepancy rather than choosing silently.
### 5. Include practical implementation details
When practical/code content exists, include:
- objective of the demo
- Setup requirements
- Commands used
- Libraries/packages
- Important classes/functions
- 
Step-by-step pipeline
- Inputs and outputs
- Model names only if present in source
- Hyperparameters only if present in source
Train/eval split only if present in source
-Saving/loading/inference/evaluation steps only if present in source
Common errors or instructor warnings
### 6.
Include examples
Extract examples mentioned by the instructor or shown in materials.
- Explain what each example demonstrates.
Do not add new examples unless clearly labeled as
"extra illustration" and only if the user permits external clarification.
- If user says "use only sources," do not add extra examples.
### 7. Capture references and resources
mentioned
when the transcript, slides, handwritten notes, or discussion mention research papers, Google searches, websites, documentation pages, Github repositories, Hugging Face pages, model cards, datasets, or other external resources:
- Extract and list all explicitly mentioned
external references.
- Capture the reference exactly as discussed when available:
- Paper title
- Website/documentation name
- GitHub repository name
- Hugging Face model/dataset name
Model card name
Dataset name
Search query used by the instructor
- URL if provided in the source
Do not invent URLs, repository names, paper titles,
model
names,
dataset names, or links.
If only a search query was shown or spoken,
record it as a **search query mentioned**, not as a verified link.
If the instructor says
"search this on Google" or shows a search term,
include that
term under
**Search Terms Mentioned**.
If a GitHub repo, notebook, or resource folder is mentioned but the exact link is not provided, write:
"repo mentioned, exact URL not available in source."
- If a paper is mentioned informally but the title is incomplete, write the partial title and mark it as incomplete.
- Briefly explain why each resource was mentioned and what topic it supports.
Mark each reference as:
**Used**
**Mentioned**
**Deferred**
**Incomplete**
**Search term only**
- **Link unavailable**
- Use only the provided transcript/materials by default.
-Do not perform web search unless the user explicitly asks for external research or web-based enrichment.
- If web search is not used, state that references are captured only from the provided class sources.
### 8. Include Q&A section
- Rewrite student doubts as clean questions.
- Give concise answers based only on the instructor's response.
- If the instructor's answer was incomplete, say so.
- Group repeated questions together.
- Separate technical Q&A from career/admin/general Q&A when useful.
### 9. End with learning support
Include:
- Glossary
- Revision checklist
- Practice tasks
- Open gaps
- Deferred topics / next-class dependencies
- Optional exam/interview focus if user requested it
## Default output structure
Use this structure unless the user requests a different one:
# Title
## Class Overview
- Session topic
- Main outcomes
- What a student should understand after reading
## Source Files Used
Table with:
- Source file/name
- туре
- How it was used
- Limitations/gaps
## Lecture Roadmap
Table with:
- Approx. time / section
- Topic
- What happened
## Core Concepts
- Main theory
- Definitions
- Diagrams converted into text
- Concept relationships
## Practical Pipeline
- Setup
- Commands
- Workflow
- Inputs/outputs
- Instructor warnings
## Code/Notebook Concepts
- Libraries
- Classes/functions
- Parameters
- Execution flow
- What the code is meant to do
## Domain Material Summary
- Formal definitions and domain-specific facts from slides/PDFs/handwritten notes
- Separate from casual mentions
## Examples Discussed
- Example
- Why it was used
-
What it teaches
## References and Resources Mentioned
Use separate subsections where applicable:
- Research Papers Mentioned
- Search Terms Mentioned
- GitHub Repositories Mentioned
- Hugging Face Models/Datasets Mentioned
- Documentation/Websites Mentioned
- Course/Dashboard Resources Mentioned
Recommended table:
| Type | Reference / Search Term Context Status l
Research paper Name of paper, if available Why it was mentioned Taught / Mentioned / Deferred / Incomplete I
| GitHub repo Repo name or URL it provided What it contains Mentioned / Used / Link unavailable
1 Search term Exact search query | what instructor searched for | Search term only I
¡ Hugeing face | Model or dataset name | How it relates to class | Mentioned / used !
Documentation | Website or docs name | What concept it supports | Mentioned / Used |
| Course resource | Dashboard/GitHub/resource name | What students should use it for | Mentioned / Used |
## Doubt Session Q&A
- Clean question
- Instructor-based answer
## Glossary
- Term
- Simple meaning
- Class-specific context
## Revision Checklist
- Actionable checkboxes
## Practice Tasks
- Short tasks for revision
- Assignment-style tasks if applicable

## Open Gaps
- Missing/unreadable source parts
- Topics mentioned but not covered
- Topics deferred to later class
- External references mentioned without complete links/titles
## Markdown/File Output Rules
- If the user asks for a Markdown file, produce clean Markdown content suitable to save as.md.
- If file creation is available, create the requested file at the end after synthesizing all notes.
- If direct file creation is not available, clearly say so and provide the complete Markdown content.
- Use fenced code blocks only for actual code/commands or when giving full file content.
- Keep headings consistent and navigable.
## Citation and Source Handling
- If source citations are available, cite factual claims inline.
- Cite definitions, model names, commands, diagrams, and source-specific claims..
- Do not cite every bullet if the whole paragraph/list is from the same source; cite the introductory sentence where appropriate.
- Include source references in tables when claims come from. specific files.
Do not reveal or reference non-readable/internal source mechanics.
If a source is empty or unreadable, state only that no usable content was available from that file.
- If a URL is present in the source, preserve it exactly as given.
Do not. fabricate or normalize missing URLS.
## Guardrails
-Do not present domain material as professional, legal, medical, financial, or investment advice.
Do not fabricate notebook code, links, model names,
datasets, commands, screenshots, demos, formulas, or instructor claims.
- Do not fabricate research paper titles, Github repositories, Hugging Face pages, search results, documentation links, or URLS.

- Do not add external knowledge when the user says to use only provided sources.
- If the instructor says a topic will be covered later, mark it as deferred.
- Keep notes readable; avoid dumping transcript text.
- Remove unrelated admin chatter unless it affects assignments, deadlines, resources, or next steps.
- Preserve important instructor warnings and practical caveats.
- Be explicit about uncertainty, OCR errors, missing files, incomplete transcript sections, or incomplete references.







GIRISH KUMAR KONERU
Bangalore
