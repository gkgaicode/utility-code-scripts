
# RAG Expert Notes

This Markdown contains the structured notes produced from the Zoom session.

## Contents

- Module Overview
- Where RAG Fits in GenAI
- Why RAG is Important
- Definition of RAG
- Retrieval, Augmentation, Generation
- Classical RAG Pipeline
- Data Ingestion
- Retrieval
- Generation
- Why RAG is Needed
- Hallucinations
- RAG vs Fine-tuning
- Chunking
- Embeddings
- Vector Database
- Similarity Search
- Data Sources
- Data Modalities
- LangChain vs LangGraph
- Future Topics
- Vectorless RAG
- Practical Learning Roadmap
- Key Takeaways

> Note: This file is a Markdown version of the structured notes generated in chat. You can extend it by pasting the detailed sections from the conversation if you want a full book-length document.

I analyzed the uploaded Zoom notes. This session is essentially the **first conceptual lecture of the RAG (Retrieval-Augmented Generation) module**. The instructor repeatedly emphasizes understanding the **fundamentals and architecture** before writing any code.

Below are the notes reorganized as they would appear in a GenAI textbook rather than a Zoom transcript.

---

# Retrieval-Augmented Generation (RAG)

## Expert Notes (Structured Learning)

# Module Overview

This chapter introduces one of the most important concepts in modern Generative AI.

Unlike Fine-tuning, RAG does **not train the LLM**.

Instead, it provides the LLM with **relevant external knowledge** before asking it to generate an answer.

---

# Where RAG Fits in GenAI

According to the course flow:

```
Generative AI

│
├── Encoding
│
├── Embeddings
│
├── Transformer Architecture
│
├── LLM APIs
│
├── Fine-tuning
│
├── RAG   ← Current Module
│
├── Agentic AI
│
├── Prompt Engineering
│
├── Evaluation
│
├── Guardrails
│
└── MCP
```

The instructor mentions spending approximately:

* 3 months on foundations
* 8–10 classes on Fine-tuning
* 6–8 classes on RAG
* Followed by Agentic AI

---

# Why RAG is Important

The instructor clearly mentions:

> Fine-tuning is NOT the most common work in industry.

Most real-world GenAI applications involve

* Chatbots
* Enterprise Search
* Knowledge Assistants
* Company Q&A
* Document Search

These are almost always built using RAG.

---

# Definition of RAG

RAG stands for

```
Retrieval
Augmentation
Generation
```

---

## Retrieval

Retrieve relevant information from external data.

Examples:

* PDFs
* Word documents
* Websites
* Databases
* Internal company documents
* Knowledge Bases

---

## Augmentation

Augmentation means

> Enrich the user's prompt by adding retrieved context.

Instead of

```
User Question
```

the model receives

```
Context

+

User Question

+

Instructions
```

---

## Generation

The LLM generates the answer using

* User question
* Retrieved context
* Prompt instructions

---

# One-Line Interview Definition

> RAG is a technique that retrieves relevant external knowledge and provides it as context to an LLM before generating the final response.

---

# Core Philosophy of RAG

The instructor repeatedly emphasizes:

> "LLM doesn't know everything."

Therefore,

```
Instead of retraining the model

↓

Give the model the required information
before asking the question.
```

---

# Classical RAG Pipeline

```
                DATA SOURCES

                     │

               Data Parsing

                     │

                Chunking

                     │

               Embedding

                     │

            Vector Database

                     │
──────────────────────────────────

User Question

      │

Embedding

      │

Similarity Search

      │

Relevant Chunks Retrieved

      │

Context

+

Question

+

Instructions

      │

LLM

      │

Generated Answer
```

---

# Two Major Parts of RAG

The instructor divides the entire pipeline into two sections.

## Part 1

### Ingestion & Indexing

Responsible for preparing knowledge.

Includes

* Reading documents
* Parsing
* Chunking
* Embeddings
* Vector Database

---

## Part 2

### Retrieval & Generation

Responsible for answering questions.

Includes

* Similarity Search
* Retrieving Context
* Prompt Augmentation
* LLM Response

---

# Three Major Components

The instructor simplifies RAG into three components.

## 1. Data Ingestion

Responsible for creating the knowledge base.

Includes

* Data Parsing
* Chunking
* Embeddings
* Vector Database

---

## 2. Retrieval

Responsible for finding the correct information.

Main task:

```
User Query

↓

Embedding

↓

Similarity Search

↓

Relevant Chunks
```

---

## 3. Generation

LLM generates the answer using

```
Prompt

+

Retrieved Context

+

User Query
```

---

# Difficulty Level

According to the instructor:

## Difficult Areas

### Data Parsing

Reasons:

* Different document formats
* Tables
* Images
* OCR
* Metadata
* Layout understanding

---

### Retrieval

Reasons

Need to retrieve

the correct chunk

not

just any chunk.

Retrieval quality determines

the final answer quality.

---

## Easier Part

Generation

Because

modern LLMs already possess excellent reasoning capability.

The main work is prompt design.

---

# What is Data Ingestion?

Pipeline:

```
Raw Documents

↓

Parsing

↓

Chunking

↓

Embeddings

↓

Vector Database
```

---

# What is Retrieval?

```
User Question

↓

Embedding

↓

Similarity Search

↓

Top Relevant Chunks
```

---

# What is Augmentation?

```
Question

+

Retrieved Context

+

Instructions

↓

LLM
```

---

# What is Generation?

```
LLM

↓

Grounded Response
```

---

# Example

User asks

```
What is our refund policy?
```

LLM alone

```
May hallucinate.
```

With RAG

Retrieve from company policy

```
Refunds allowed within 7 days.
```

Prompt becomes

```
Context

Refunds allowed within 7 days.

Question

What is our refund policy?
```

LLM now produces

```
Refunds are allowed within 7 days.
```

---

# Why RAG is Needed

The instructor explains four major reasons.

## 1. Private Data

LLMs are NOT trained on

* Company documents
* Internal databases
* Enterprise knowledge

RAG connects the LLM with that information.

---

## 2. Latest Information

LLMs have knowledge cutoffs.

Example

Current temperature

Current company policies

Latest products

Latest regulations

Need retrieval.

---

## 3. Hallucination Reduction

Hallucination

=

LLM confidently gives the wrong answer.

Example

LLM

```
Refund period = 30 days
```

Company document

```
Refund period = 7 days
```

Using RAG

The answer is grounded in retrieved documents.

---

## 4. Avoid Continuous Fine-tuning

If documents change

Every day

Every week

Every month

Fine-tuning becomes expensive.

Instead

Simply update

```
Documents

↓

Vector Database
```

No retraining required.

---

# RAG vs Fine-tuning

| RAG                        | Fine-tuning                            |
| -------------------------- | -------------------------------------- |
| Adds external knowledge    | Changes model behaviour                |
| No weight updates          | Model weights change                   |
| Lower cost                 | Higher cost                            |
| Easy document updates      | Retraining required                    |
| Best for enterprise search | Best for behaviour/style customization |

---

# Chunking

Definition

Breaking a large document into smaller meaningful pieces.

Instructor notes

Chunking is sometimes optional depending on use case.

---

# Embeddings

Convert text into vectors.

Both

Documents

and

User Queries

are converted into embeddings.

Similarity search happens on embeddings.

---

# Vector Database

Purpose

Store embeddings.

Examples (to be covered later)

* Chroma
* FAISS
* Pinecone
* Milvus
* Weaviate

---

# Similarity Search

Process

```
Query Embedding

↓

Compare with Document Embeddings

↓

Retrieve nearest vectors

↓

Return relevant chunks
```

---

# Data Sources

The instructor mentions RAG can retrieve from

* PDFs
* DOCX
* CSV
* JSON
* HTML
* SQL
* Internal Databases
* Company Portal
* Websites
* Cloud Storage
* Images
* Audio
* Video

---

# Data Modalities

Nature of data

```
Text

Images

Audio

Video
```

Most RAG systems initially focus on

* Text
* Images

---

# File Formats

Examples

```
PDF

DOCX

CSV

JSON

YAML

HTML

MP3

MP4
```

---

# Data Structures

The instructor classifies data as

Structured

* SQL
* CSV
* Excel

Semi-structured

* JSON
* YAML
* HTML

Unstructured

* PDF
* Images
* Audio
* Video

---

# LangChain vs LangGraph

Instructor recommendation

Focus only on

* LangChain
* LangGraph

Avoid trying many frameworks simultaneously.

Reason

Concepts matter more than frameworks.

---

# Framework Usage

## LangChain

Used for

* Classical RAG
* Document loading
* Embeddings
* Retrieval
* Prompt chains

---

## LangGraph

Used for

* Agentic RAG
* Multi-agent workflows
* Orchestration
* Memory
* State management

---

# Future Topics Mentioned

The instructor plans to cover

* Document AI
* OCR
* Data Parsing
* Metadata
* Chunking Strategies
* Vector Databases
* Similarity Search
* Retrieval Pipelines
* Prompt Engineering
* Advanced RAG
* Memory
* Evaluation
* Guardrails
* Vectorless RAG
* Agentic RAG
* MCP Integration

---

# Vectorless RAG

The instructor briefly introduces Vectorless RAG.

Instead of

```
Embedding

↓

Vector Database
```

It retrieves directly from documents using traditional retrieval methods such as keyword-based search (e.g., BM25).

Important takeaway:

* Vectorless RAG is **not a replacement** for vector-based RAG.
* It may work well for some use cases but should be evaluated based on retrieval quality.

---

# Practical Learning Roadmap (Instructor Plan)

```
RAG

│
├── Introduction
│
├── Why RAG?
│
├── RAG Pipeline
│
├── RAG vs Fine-tuning
│
├── Data Parsing (Document AI)
│
├── Chunking
│
├── Embeddings
│
├── Vector Databases
│
├── Retrieval
│
├── Similarity Search
│
├── Prompt Engineering
│
├── Generation
│
├── Advanced RAG
│
├── Agentic RAG
│
└── MCP Integration
```

## Key Takeaways

1. **RAG is a pipeline, not an LLM or a model.**
2. **The three pillars of RAG are Data Ingestion, Retrieval, and Generation.**
3. **The most challenging production problems are data parsing and accurate retrieval; generation is comparatively easier due to strong modern LLM reasoning.**
4. **RAG is preferred over fine-tuning for enterprise knowledge, frequently changing data, and private documents.**
5. **Mastering concepts such as embeddings, vector databases, similarity search, and prompt augmentation is more valuable than learning many frameworks.**
6. **LangChain is the primary framework for classical RAG, while LangGraph becomes important for Agentic RAG and orchestration.**

These notes preserve the instructor's explanations but reorganize them into a structured, reference-style guide suitable for revision or interview preparation.


Yes. Although this first RAG lecture was mostly conceptual, the instructor did mention several libraries, frameworks, SDKs, and technologies. Here's a structured summary.

| Category                | Library/Framework | Context in the Zoom Notes                                                                         |
| ----------------------- | ----------------- | ------------------------------------------------------------------------------------------------- |
| ⭐ Primary RAG Framework | **LangChain**     | Main framework for building classical RAG pipelines. Will be used throughout the course.          |
| ⭐ Agentic AI Framework  | **LangGraph**     | Will be introduced later for Agentic RAG, orchestration, workflows, memory, and state management. |
| SDK                     | **OpenAI SDK**    | Instructor mentioned using it in one of his POCs.                                                 |
| Agent Framework         | **CrewAI**        | Mentioned only for comparison. Instructor said it isn't necessary to learn initially.             |
| Agent Framework         | **AutoGen**       | Mentioned similarly to CrewAI. Not required for this course.                                      |
| Model                   | GPT-5.x           | Used as an example LLM inside a RAG pipeline.                                                     |
| Model                   | Claude            | Mentioned as another LLM that can be plugged into RAG.                                            |
| Model                   | Gemini            | Mentioned as another supported LLM.                                                               |
| API Framework           | **FastAPI**       | Mentioned later while answering a student's question about APIs. Used to expose RAG services.     |
| Protocol                | MCP               | Mentioned as a future topic. Context from RAG can later be exposed through MCP connectors.        |

---

## Libraries/frameworks that will be taught later (mentioned but not yet covered)

The instructor said future practical sessions will include:

### Data Parsing (Document AI)

He mentioned that libraries for parsing documents would be introduced in later classes, but **their names were not given in this lecture**.

Topics include:

* PDF parsing
* DOCX parsing
* Images
* OCR
* Tables
* Metadata extraction

---

### Vector Databases

He said vector databases will be covered in upcoming sessions but **did not mention any specific database names** in this lecture.

---

### Retrieval

Topics to be covered:

* Similarity Search
* Retrieval Pipeline
* Embeddings
* Chunking
* Indexing

---

## Technologies mentioned

These are concepts rather than libraries:

* Embeddings
* Transformer Architecture
* Similarity Search
* Vector Database
* Vectorless RAG
* Document AI
* OCR
* Prompt Engineering
* Fine-tuning
* Agentic RAG
* Guardrails
* Evaluation
* Memory
* State Management

---

## Instructor's recommendation

One of the key messages in the lecture was:

> Don't try to learn 5–6 frameworks at once. Master one framework first, build applications with it, and then explore others.

The instructor specifically recommended focusing on:

1. **LangChain** (primary framework)
2. **LangGraph** (for Agentic AI)

He explicitly stated that he has built production systems primarily using these frameworks and has not needed to rely on frameworks like CrewAI or AutoGen for his work.

### Summary

The libraries/frameworks explicitly mentioned in this Zoom session are:

* **LangChain** ✅ (primary focus)
* **LangGraph** ✅ (primary focus for Agentic AI)
* **OpenAI SDK**
* **CrewAI** (comparison only)
* **AutoGen** (comparison only)
* **FastAPI**
* **MCP** (future topic)

No specific document parsing libraries (such as PyMuPDF, Unstructured, or LangChain document loaders) or vector databases (such as Chroma, FAISS, or Pinecone) were named in this lecture—they were only mentioned as upcoming topics.


Based on the Zoom notes you uploaded, **no specific document parsing libraries were discussed by name**.

The instructor **mentioned that document parsing libraries will be covered in upcoming classes**, but did not identify any particular libraries in this session.

### What was actually discussed

The instructor introduced **Data Parsing (Document AI)** as the **first component of the Data Ingestion pipeline**.

The topics mentioned include:

* Data Parsing
* Document AI
* OCR (for scanned documents/images)
* Metadata extraction
* Parsing different document types:

  * PDF
  * DOCX (Word)
  * Images
  * Tables
  * HTML
  * CSV
  * JSON
* Different data modalities:

  * Text
  * Images
  * Audio
  * Video
* Different storage formats:

  * PDF
  * DOCX
  * CSV
  * JSON
  * YAML
  * HTML
  * MP3
  * MP4

He also said:

> "I will show you what library we are going to use for parsing the document."

and

> "I'll show you metadata and all everything."

However, **he stopped before naming any libraries**, indicating they would be introduced in the practical sessions.

---

## Libraries **not** mentioned in this lecture

The following popular document parsing libraries **were not mentioned** in the transcript:

* **PyMuPDF (fitz)**
* **pdfplumber**
* **PyPDF2**
* **pypdf**
* **Unstructured**
* **LlamaParse**
* **Apache Tika**
* **python-docx**
* **camelot**
* **tabula-py**
* **OCR libraries** such as **Tesseract**, **EasyOCR**, or **PaddleOCR**

---

## Likely libraries based on a typical LangChain RAG course (not stated in the lecture)

Although they were **not mentioned**, many LangChain RAG courses commonly use:

| Purpose                     | Common Libraries                       |
| --------------------------- | -------------------------------------- |
| PDF parsing                 | PyMuPDF, pypdf, pdfplumber             |
| DOCX parsing                | python-docx                            |
| General document parsing    | Unstructured                           |
| Enterprise document parsing | LlamaParse                             |
| OCR                         | Tesseract, EasyOCR, PaddleOCR          |
| Tables                      | Camelot, Tabula-py                     |
| LangChain integration       | `langchain_community.document_loaders` |

These are **industry-standard choices**, but they were **not explicitly discussed** in the Zoom session.

### Conclusion

From this particular lecture:

* ✅ **Document AI** was introduced as a concept.
* ✅ **Data Parsing** was identified as a major part of the RAG ingestion pipeline.
* ✅ The instructor promised to demonstrate parsing libraries in later practical classes.
* ❌ **No document parsing library names were actually mentioned** in the transcript you provided.

