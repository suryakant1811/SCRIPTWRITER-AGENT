# 🎬 Content Script Agent

An Agentic AI project built using **LangGraph** that transforms a rough content idea into a polished Hinglish video script through a multi-stage workflow.

Instead of asking one LLM to do everything, this project assigns a specific responsibility to each AI node. Every node performs one task, updates the shared state, and passes it to the next node.

---

# Project Goal

Create an AI pipeline capable of transforming a rough script into a professional YouTube-ready Hinglish script.

Current Workflow:

```
Topic
   │
   ▼
Draft Writer
   │
   ▼
Editor
   │
   ▼
Script Writer
   │
   ▼
Hinglish Converter
   │
   ▼
Final Output
```

Each stage improves the quality of the content before handing it to the next stage.

---

# Why LangGraph?

Instead of putting every prompt inside one large LLM call, LangGraph allows us to split the work into independent nodes.

Benefits include:

* Better code organization
* Easier debugging
* Reusable AI components
* Simple workflow expansion
* Production-style architecture

---

# Project Structure

```
content-script-agent/
│
├── README.md
├── requirements.txt
├── main.py
├── state.py
│
├── graph/
│   └── content_workflow.py
│
└── nodes/
    ├── draft_writer.py
    ├── editor.py
    ├── script_writer.py
    └── hinglish_converter.py
```

---

# Folder Explanation

## main.py

The starting point of the application.

Responsibilities:

* Creates the workflow
* Sends the initial input
* Executes the graph
* Displays the final result

Think of this as the **CEO** of the application.

---

## state.py

Defines the shared state that travels through every node.

Think of it as a **backpack**.

Every node:

* Reads information from the backpack
* Adds or updates information
* Passes the backpack to the next node

---

## graph/content_workflow.py

Builds the LangGraph workflow.

Responsibilities:

* Creates the graph
* Registers all nodes
* Connects nodes together
* Defines where execution starts and ends

Think of it as the **manager** deciding which employee works next.

---

## nodes/

Each file inside this folder represents one AI worker.

Every node has only one responsibility.

### draft_writer.py

Creates the first draft from the provided topic.

Input:

* Topic

Output:

* Draft Script

---

### editor.py

Improves:

* Grammar
* Sentence structure
* Readability
* Tone

Output:

* Edited Script

---

### script_writer.py

Transforms the edited draft into an engaging video script.

Responsibilities include:

* Strong hook
* Better storytelling
* Smooth transitions
* Viewer engagement

---

### hinglish_converter.py

Converts the script into natural Hinglish while preserving the meaning and flow.

---

# Learning Objectives

This project is designed to teach:

* LangGraph fundamentals
* State management
* Node design
* Workflow creation
* AI pipeline architecture
* Prompt engineering
* Modular code organization

Rather than building one large prompt, this project demonstrates how to decompose a complex task into smaller, specialized AI workers.

---

# Future Improvements

The current project is intentionally simple.

Future versions may include:

* Research Agent
* Fact Checker
* SEO Optimizer
* Thumbnail Prompt Generator
* Title Generator
* Human Review
* Memory
* Tool Calling
* Multi-Agent Collaboration

---

# Key Concept

Every node follows the same pattern:

```
Read State
      │
      ▼
Do One Job
      │
      ▼
Update State
      │
      ▼
Pass State Forward
```

Understanding this simple pattern is the foundation of building more advanced Agentic AI systems.

---

# Tech Stack

* Python
* LangGraph
* LangChain
* Google Gemini
* Pydantic
* Python Virtual Environment (venv)

---

# Educational Purpose

This repository is built as a learning project to understand how modern Agentic AI systems are designed. The focus is on understanding architecture, state flow, and modular AI workflows rather than simply generating content.
