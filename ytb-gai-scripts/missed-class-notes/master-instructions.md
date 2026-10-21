---
name: missed-class-notes
description: >
  Convert class transcripts and supporting learning materials into accurate,
  complete, structured, revision-friendly study notes. Use when the user
  provides YouTube transcripts, VTT/SRT/TXT files, copied speech, PDFs, slides,
  handwritten notes, screenshots, notebooks, code files, research references,
  GitHub repositories, Hugging Face resources, or course materials and requests
  study notes, revision notes, missed-class understanding, summaries, or a
  Markdown notes file.
---

# Missed Class Notes — Instructions

## 1. Objective

Turn messy class artifacts into readable, structured, technically accurate study notes.

The notes must help a student who missed the session understand the lecture without watching the entire recording.

Preserve all meaningful concepts, definitions, examples, demonstrations, implementation details, instructor warnings, student questions, answers, and learning resources.

Produce **study notes, not merely a transcript cleanup or a short summary**.

## 2. Supported Inputs

### 2.1 Transcripts and spoken content
- YouTube transcripts and copied speech text
- `.vtt` WebVTT captions
- `.srt` SubRip subtitles
- `.txt` text files
- Chat logs and discussion transcripts
- Rough lecture notes and timing annotations

### 2.2 Class materials
- PDF documents
- PowerPoint presentations (`.pptx`)
- Jupyter notebooks and other notebook files
- Source code and configuration files
- Screenshots and images
- Handwritten notes
- Assignments, handouts, and reference documents

### 2.3 Optional context
- Class number and date
- Student's current knowledge or education level
- Target exam, interview, assignment, or project
- Preferred depth and language
- Instructor-provided resource links
- Rough timing notes and additional student observations

Use optional context to tailor the presentation. Do not let it introduce unsupported class content.

## 3. Core Operating Principles

1. **Inspect first, synthesize second.** Examine the available sources before writing the notes.
2. **Preserve coverage.** Do not silently omit meaningful concepts, examples, questions, or implementation details.
3. **Follow the lecture's logic.** Prefer the transcript for topic order, teaching sequence, instructor emphasis, demonstrations, and Q&A.
4. **Respect source authority.** Use slides and formal documents for definitions, formulas, terminology, and diagrams; use notebooks and code for implementation specifics.
5. **Separate evidence from interpretation.** Clearly distinguish what was taught, briefly mentioned, deferred, unclear, or inferred from source structure.
6. **Do not invent content.** Never fabricate facts, examples, code, model names, links, results, or instructor statements.
7. **Make notes revision-friendly.** Organize material for quick review before exams, interviews, assignments, and projects.
8. **Preserve useful detail.** Remove filler and repetition, but not information that contributes to understanding.
9. **Record uncertainty explicitly.** Flag missing, unreadable, contradictory, or ambiguous information.
10. **Use provided sources by default.** Do not browse or enrich notes with external knowledge unless the user explicitly requests external research.

## 4. Source Inspection and Evidence Handling

### Step 1 — Inventory the available sources

Identify every supplied source and classify it as applicable:

- Transcript or captions
- Slides, PDF, or handwritten notes
- Notebook or code files
- Images and screenshots
- Research papers and references
- GitHub repositories
- Hugging Face models or datasets
- Documentation and websites
- Search terms or search results included in the materials
- Course dashboards, resource folders, and assignments
- Timing notes and user comments

Create a source inventory before synthesis.

For each source, record:
- File name or reference
- Source type
- Information extracted
- How it contributes to the notes
- Limitations or missing information

If a source is empty, unreadable, incomplete, or mostly dependent on uncertain OCR, state the limitation briefly.

If an expected source is missing, do not guess its contents.

### Step 2 — Apply source-specific priorities

| Source | Primary purpose |
|---|---|
| Transcript | Lecture flow, explanations, instructor emphasis, spoken examples, demonstrations, and Q&A |
| Slides/PDF | Formal definitions, diagrams, formulas, terminology, and structured domain material |
| Handwritten notes/images | Additional explanations, diagrams, annotations, and class-specific observations |
| Notebook/code | Imports, libraries, commands, functions, classes, parameters, execution order, and outputs |
| Assignments/handouts | Tasks, deliverables, constraints, deadlines, and assessment requirements |
| Resource references | Exact paper titles, repository names, model/dataset identifiers, documentation, URLs, and search terms |
| Timing notes | Approximate section boundaries and significant events, subject to transcript verification |

When multiple sources overlap, consolidate them without duplicating content.

When sources disagree, document the discrepancy and identify which source supports each version. Do not silently select one.

## 5. Transcript Extraction and Cleaning

### VTT, SRT, and TXT processing

1. Inspect the complete available transcript.
2. Identify timestamps and construct a preliminary lecture map.
3. Group related speech into coherent topics.
4. Correct obvious transcription and punctuation errors when the intended meaning is sufficiently clear.
5. Remove filler words, redundant repetition, false starts, greetings, and unrelated administrative chatter.
6. Preserve technically meaningful repetition, emphasis, warnings, and examples.
7. Retain timestamps for major topic changes, demonstrations, breaks, and Q&A when available.
8. Remove unnecessary timestamps from the final prose while keeping useful navigation points.
9. Preserve meaningful lecture order and dependencies.
10. Mark unclear technical terms or incomplete statements rather than guessing.

### Mixed-language and Hinglish transcripts

- Convert to polished English by default unless another language is requested.
- Preserve technical terms, API names, identifiers, commands, and model names exactly.
- Retain original wording when translation could change the meaning.
- Mark genuinely ambiguous speech rather than inventing a translation.

### Long transcripts

Process the complete available source systematically.

Use section-by-section extraction and a coverage checklist when necessary. Consolidate the sections only after ensuring that important concepts have not been lost.

Do not claim that a transcript is complete if only a partial source was available.

## 6. Lecture Roadmap

Create a lecture roadmap before developing detailed notes.

Include applicable sections:

- Introduction and objectives
- Administrative information relevant to learning
- Assignment or previous-class discussion
- Main lecture concepts
- Demonstrations and practical walkthroughs
- Breaks, when relevant
- Recap and key takeaways
- Doubt/Q&A session
- Deferred topics and next-class dependencies

Use a table with these columns:

| Approx. timestamp | Topic or section | What was covered |
|---|---|---|

Use approximate timestamps only when supported by the source.

If user-provided timing notes conflict with transcript timestamps, record the discrepancy and prefer transcript evidence unless the user instructs otherwise.

## 7. Concept Synthesis and Coverage Labels

Organize notes from the high-level overview to detailed explanations.

Use these labels consistently:

- **Taught in detail** — Substantive explanation, demonstration, or worked example was provided.
- **Mentioned briefly** — The topic was named or discussed without substantial explanation.
- **Deferred to later class** — The instructor explicitly postponed the topic.
- **Unclear from source** — The available material does not support a reliable interpretation.
- **Source discrepancy** — Two or more supplied sources conflict.

For each important concept, include the applicable details:

1. Concept name
2. Definition or explanation
3. Purpose and significance
4. How it works, as explained in class
5. Relationships to other concepts
6. Instructor-provided examples
7. Practical applications discussed
8. Important limitations or warnings
9. Coverage status, where useful

Explain concepts in beginner-friendly but technically accurate language without changing the instructor's intended meaning.

Use tables for comparisons, numbered steps for workflows, bullets for key facts, and diagrams expressed as text when useful.

Do not expand a brief mention into a detailed tutorial using outside knowledge.

## 8. Practical and Implementation Details

Whenever the class contains practical work, demonstrations, or code, capture the following where available.

### 8.1 Demonstration overview
- Objective of the demonstration
- Problem being solved
- Setup and prerequisites
- Inputs and expected outputs
- Execution sequence
- Observed results
- Instructor warnings and troubleshooting guidance

### 8.2 Technical implementation
- Programming language and version
- Libraries, frameworks, and packages
- Imports
- Commands and configuration
- Classes, functions, methods, and parameters
- Model names and versions
- Hyperparameters
- Dataset details
- Training and evaluation split
- Saving, loading, inference, and evaluation steps
- Error messages and fixes
- Assumptions and environment constraints

Include each item only when supported by the supplied material.

### 8.3 Practical pipeline

Present the execution sequence as numbered steps.

For example, when supported by the class:

1. Prepare the environment.
2. Load the required inputs.
3. Execute the processing steps.
4. Run the model or application.
5. Inspect the output.
6. Evaluate the result.
7. Save or deploy the result.

This sequence is a formatting template, not permission to invent steps missing from the class.

### 8.4 Code accuracy

- Preserve original code identifiers, commands, package names, and parameters.
- Explain code only to the extent supported by the source.
- Never fabricate notebook cells, outputs, execution results, or configuration values.
- If code is incomplete, identify the missing portion.
- Separate exact source code from explanatory pseudocode.
- If a correction is necessary to make a supplied example understandable, distinguish the correction from the original material.

## 9. Examples and Demonstrations

Extract all meaningful instructor examples and explain their purpose.

For each example, include:

- **Example:** What the instructor demonstrated or described.
- **Context:** Which concept it relates to.
- **Process:** How the example was explained or executed.
- **Outcome:** What result was reported or shown.
- **Learning point:** What the example teaches.

Do not add new examples by default.

If the user explicitly permits external clarification, label any added illustration as **Extra illustration — not part of the original class**.

If the user requests source-only notes, use only the provided material.

## 10. Research References and Learning Resources

Capture all explicitly mentioned resources from transcripts, slides, notes, screenshots, notebooks, and supplied reference text.

### Resource categories

- Research papers and publications
- Google/search terms and queries
- GitHub repositories and source code
- Hugging Face models, datasets, and model cards
- Documentation pages and technical websites
- Course dashboards and learning platforms
- Notebooks, resource folders, and assignments
- Other named tools, frameworks, and educational resources

### Capture requirements

For each reference, preserve available information exactly:

- Resource type
- Exact name or partial name
- URL, if present in the source
- Search query, if applicable
- Context in which it was mentioned
- Purpose or concept it supports
- Whether it was used in the demonstration, merely mentioned, or deferred
- Any missing information

Use these status labels where applicable:

- **Used**
- **Mentioned**
- **Deferred**
- **Incomplete**
- **Search term only**
- **Link unavailable**

### Resource integrity rules

1. Never invent URLs, paper titles, repository names, model names, dataset names, or resource links.
2. Preserve provided URLs exactly; do not silently normalize or replace them.
3. If a repository is mentioned but no URL is supplied, write: "Repository mentioned; exact URL not available in source."
4. If only a search query is spoken or displayed, record it under **Search Terms Mentioned**.
5. If a paper title is incomplete, preserve the available title and mark it incomplete.
6. If a resource is referenced informally, do not claim that its identity has been verified.
7. Briefly explain why each resource was mentioned, using only the available class context.
8. Do not treat every named resource as one that the instructor actually used.

**External research policy:** Do not browse the web unless the user explicitly asks for external research, link verification, or web-based enrichment. When no web research is performed, state that the resource list reflects only the supplied class sources.

## 11. Doubt Session and Q&A

Extract meaningful questions and answers from the lecture.

For each item:

- Rewrite the student's question clearly without changing its meaning.
- Summarize the instructor's answer accurately.
- Include relevant examples or qualifications.
- Group repeated questions together when appropriate.
- Distinguish technical questions from career, administrative, and general questions.
- Mark incomplete or unclear answers explicitly.

If the instructor did not answer a question, state that no complete answer was available in the source.

Do not independently answer unresolved questions unless the user requests external clarification.

## 12. Domain Material and Formal Definitions

When slides, PDFs, handwritten notes, or other formal materials provide domain-specific information:

- Preserve formal definitions and terminology.
- Capture formulas and their variable meanings when legible.
- Convert diagrams into clear textual representations.
- Explain relationships between components.
- Preserve important assumptions, conditions, and limitations.
- Distinguish formal source material from informal spoken explanations.
- Identify unreadable formula symbols or uncertain OCR.

Do not silently replace the supplied definition with an external or supposedly more standard definition.

If the transcript and slides provide different definitions, report the difference.

## 13. Learning and Revision Support

End the notes with the following sections.

### 13.1 Glossary

| Term | Simple meaning | Context in the class |
|---|---|---|

Include important technical terms, acronyms, methods, tools, and concepts actually present in the source.

### 13.2 Revision checklist

Create actionable checkboxes for the important learning objectives.

Examples of checklist wording:

- [ ] Explain the main concept in my own words.
- [ ] Distinguish the related concepts covered in class.
- [ ] Reproduce the demonstrated workflow, if applicable.
- [ ] Explain the instructor's example and its outcome.
- [ ] Review unresolved questions and deferred topics.

Customize the checklist to the actual class instead of mechanically using generic items.

### 13.3 Practice tasks

Include relevant tasks such as:

- Short-answer questions
- Concept comparisons
- Explain-in-your-own-words exercises
- Code tracing or implementation exercises
- Diagram interpretation
- Assignment-oriented practice
- Interview or exam-style questions, when requested

Practice tasks must be grounded in the concepts taught.

Do not fabricate official assignments or imply that instructor-created tasks were assigned when they were not.

Clearly label newly generated revision questions as **Practice questions derived from class topics**, rather than instructor-provided questions.

### 13.4 Open gaps

Record:

- Missing or unreadable source sections
- Uncertain transcription or OCR
- Contradictory statements across sources
- Incomplete resource names or URLs
- Questions that remain unanswered
- Topics mentioned but not explained
- Topics explicitly deferred to later classes
- Missing prerequisites or next-class dependencies

## 14. Default Markdown Output Structure

Use the following structure unless the user requests a different format.

# [Class or Session Title]

## 1. Class Overview
- Session topic
- Main learning objectives
- Key takeaways
- What the reader should understand after studying the notes

## 2. Source Files Used
| Source file/name | Type | How it was used | Limitations/gaps |
|---|---|---|---|

## 3. Lecture Roadmap
| Approx. timestamp | Topic | Coverage summary |
|---|---|---|

## 4. Core Concepts
- Topic-by-topic explanations
- Definitions and terminology
- Concept relationships
- Diagrams expressed in text
- Coverage labels where useful

## 5. Practical Pipeline
- Objective
- Setup and prerequisites
- Commands and configuration
- Step-by-step workflow
- Inputs and outputs
- Errors, fixes, and instructor warnings

## 6. Code and Notebook Concepts
- Libraries and imports
- Classes and functions
- Parameters and assumptions
- Execution flow
- Outputs and interpretation
- Code gaps or limitations

Include this section when relevant. Otherwise, omit it or state that no practical code material was supplied.

## 7. Domain Material Summary
- Formal definitions
- Formulas and assumptions
- Slide/PDF material
- Diagram interpretations
- Important discrepancies

## 8. Examples Discussed
| Example | Concept demonstrated | Outcome or learning point |
|---|---|---|

## 9. References and Resources Mentioned

### Research Papers Mentioned
### Search Terms Mentioned
### GitHub Repositories Mentioned
### Hugging Face Models and Datasets Mentioned
### Documentation and Websites Mentioned
### Course and Dashboard Resources Mentioned

Recommended table:

| Type | Reference or search term | Context/purpose | Status | Link or limitation |
|---|---|---|---|---|

Include only applicable subsections.

## 10. Doubt Session Q&A

### Technical Q&A
### Career, Administrative, or General Q&A

Use the applicable subsections and preserve incomplete answers.

## 11. Glossary
| Term | Simple meaning | Class-specific context |
|---|---|---|

## 12. Revision Checklist
- [ ] Actionable revision item

## 13. Practice Tasks
- Conceptual questions
- Practical exercises
- Assignment or exam preparation, when relevant

## 14. Open Gaps and Deferred Topics
- Missing or uncertain material
- Unanswered questions
- Deferred concepts
- Incomplete references
- Next-class dependencies

### Structure adaptation rules

- Use all applicable sections, not every section mechanically.
- Do not create empty headings or repetitive filler.
- If no code or Q&A was present, do not invent either.
- Retain the same heading hierarchy across related classes for easy navigation.
- Add a table of contents when the document is sufficiently long to benefit from one.
- Use internal Markdown links only when the target heading or anchor can be determined reliably.

## 15. Markdown Formatting and File Output

When the user requests Markdown notes:

1. Produce complete, clean Markdown suitable for `.md` files.
2. Use consistent headings, bullets, tables, checkboxes, and fenced code blocks.
3. Use fenced code blocks only for actual code, commands, configuration, or explicitly requested full-file content.
4. Preserve Unicode characters, mathematical symbols, code identifiers, and non-English text correctly.
5. Save Markdown as UTF-8, preferably UTF-8 without a byte-order mark (BOM), unless another encoding is explicitly requested.
6. Use LF line endings where practical for cross-platform compatibility.
7. Avoid unnecessary formatting that renders inconsistently in GitHub, VS Code, or other Markdown viewers.
8. Escape literal Markdown syntax when it would otherwise be interpreted as formatting.
9. Do not replace valid technical symbols with approximations that change their meaning.
10. If file creation is available, create the final `.md` file after synthesis and verification.
11. Provide a link to the actual created file when available.
12. If file creation is unavailable, provide the complete Markdown content or clearly explain the limitation.

For large classes, split notes into multiple files only when useful or requested. Preserve cross-references and consistent terminology when splitting.

## 16. Source Citations and Traceability

When the source material provides identifiable references or citations:

- Cite important source-specific claims where practical.
- Prioritize traceability for formal definitions, formulas, commands, model names, demonstrations, and disputed statements.
- Include page numbers, timestamps, section identifiers, or source filenames when available.
- Avoid citing every bullet when an entire section clearly derives from the same source.
- Identify the relevant source in tables when information comes from multiple materials.
- Do not fabricate citations, page numbers, timestamps, or line references.
- Keep references traceable without making the notes difficult to read.

If only one transcript is available, do not invent citations to slides, papers, or external sources.

## 17. Guardrails and Prohibited Behaviors

Never:

- Fabricate instructor claims, facts, examples, outputs, or conclusions.
- Invent notebook code, commands, screenshots, model names, datasets, or package names.
- Fabricate research paper titles, GitHub repositories, Hugging Face resources, documentation pages, or URLs.
- Add unsupported external knowledge when the user requests source-only notes.
- Present a deferred topic as if it were taught.
- Treat an incomplete answer as a complete instructor explanation.
- Hide contradictions between supplied sources.
- Guess unreadable text without marking the uncertainty.
- Dump the raw transcript instead of synthesizing it into useful notes.
- Remove meaningful instructor warnings, assignment details, deadlines, or next steps.
- Present domain material as professional legal, medical, financial, or investment advice.
- Claim that every available source was processed when only a subset was accessible.

If a source is empty or unreadable, state only that no usable content was available from that source.

Do not reveal or refer to internal source-processing mechanics.

## 18. Final Quality Assurance

Before delivering the notes, perform a structured review.

### Coverage verification
- [ ] All accessible sources have been inspected.
- [ ] Major lecture topics appear in the notes.
- [ ] Topic order and important dependencies are preserved.
- [ ] Meaningful examples, demonstrations, and instructor warnings are retained.
- [ ] Important Q&A and assignment details are captured.
- [ ] Mentioned, deferred, and unclear topics are distinguished.
- [ ] All explicitly mentioned resources have been captured where identifiable.

### Accuracy verification
- [ ] Definitions, formulas, commands, and identifiers match the sources.
- [ ] No unsupported technical claims or invented implementation details were added.
- [ ] Conflicting sources and incomplete statements are flagged.
- [ ] Uncertain OCR and transcription have not been silently guessed.
- [ ] Links and citations are present only when supported by the material.

### Revision usability
- [ ] The notes are readable without watching the full recording.
- [ ] Headings and tables make information easy to find.
- [ ] The glossary and revision checklist reflect the actual class.
- [ ] Practice tasks are grounded in the covered concepts.
- [ ] Open gaps and deferred topics are explicit.
- [ ] The Markdown renders cleanly and the file uses the intended encoding.

## 19. Success Criteria

The final notes are successful when a student who missed the session can:

1. Understand the class's major concepts and explanations.
2. Follow the lecture's structure and reasoning.
3. Review definitions, examples, and concept relationships efficiently.
4. Understand the demonstrated workflow and code, when present.
5. Find every identifiable research paper, repository, model, dataset, search term, and learning resource mentioned in the supplied material.
6. Review questions, answers, warnings, and unresolved doubts.
7. Identify what to revise, practise, or study next.
8. Distinguish actual class content from incomplete evidence and deferred material.

**Final rule:** Prioritize completeness, factual accuracy, source traceability, and revision usefulness over brevity. Remove noise, not knowledge.
