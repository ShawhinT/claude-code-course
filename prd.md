# Claude Code Crash Course — Product Requirements Document

## Overview

A local-only, single-page web application that serves as the companion UI for the Claude Code Crash Course. Students clone the repo and run it locally to follow along with the course content. The app renders markdown lesson files as HTML and provides basic progress tracking.

## Tech Stack

- **Python** with **UV** for dependency management
- **FastAPI** with **Jinja2** templates
- All state stored in `progress.json`
- **Tailwind CSS** via CDN
- **Markdown** + **Pygments** for content rendering with code syntax highlighting

## Project Structure

```
claude-code-course/
├── app.py                  # FastAPI routes
├── progress.json           # User progress (auto-created if missing)
├── content/
│   ├── 01-intro.md
│   ├── 02-what-is-a-coding-agent.md
│   ├── 03-getting-started.md
│   └── ...
├── templates/
│   ├── index.html          # Single-page layout
├── static/
│   ├── style.css
│   └── images/
│       └── ...
└── pyproject.toml
```

## Features

### Single-Page Layout

The entire app is a single page with two panels:

- **Sidebar (left)** — scrollable list of all lessons. Shows completion checkmarks and overall progress percentage at the top.
- **Main area (right)** — displays the currently selected lesson content.

Clicking a lesson in the sidebar navigates to that lesson (full page load is fine — it's instant on localhost).

### Lesson Rendering

- Lesson content lives in `content/*.md` as markdown files.
- Files are named with a numeric prefix for ordering (e.g., `01-intro.md`).
- Markdown is converted to HTML server-side using Python's `markdown` library.
- Code blocks are syntax-highlighted using the `codehilite` extension with Pygments.
- Images from slide decks can be referenced as `![alt](/static/images/filename.png)`.

### Prev/Next Navigation

- Previous and Next buttons appear at the bottom of the lesson content.
- Buttons are disabled/hidden when at the first or last lesson.

### Progress Tracking

- Each lesson has a "Mark as complete" button/checkbox.
- Completion state is persisted to `progress.json`.
- The sidebar shows a checkmark next to completed lessons.
- A progress percentage is displayed at the top of the sidebar.

### Code Syntax Highlighting

- Fenced code blocks in markdown (e.g., ` ```python `) render with syntax coloring.
- Powered by Pygments via the `codehilite` markdown extension.
- A Pygments CSS theme is included in `static/style.css` or served inline.

## Future Features (Not in Initial Build)

- **YouTube video embedding** — each lesson will embed a timestamped clip from the full course video. Requires `video_start` and `video_end` frontmatter in the markdown files.

## Non-Goals

- No authentication or user accounts.
- No database.
- No hosting or deployment. Local only.
- No build step or frontend framework.
