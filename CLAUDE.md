# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A local-only, single-page web app for the Claude Code Crash Course. Students clone the repo and run it locally to follow along with course content. The app renders markdown lesson files as HTML with a sidebar for navigation and progress tracking.

## Tech Stack

- Python 3.13 with UV for dependency management
- FastAPI + Jinja2 templates + Uvicorn
- Tailwind CSS via CDN (no build step)
- Markdown + Pygments for content rendering with syntax highlighting
- State persisted in `progress.json` (no database)

## Commands

```bash
# Install dependencies
uv sync

# Run the dev server
uv run fastapi dev app.py

# Lint
uv run ruff check .

# Format
uv run ruff format .
```

## Architecture

- `app.py` — FastAPI routes and server entry point
- `content/*.md` — Markdown lesson files, ordered by numeric prefix (e.g., `01-intro.md`)
- `templates/index.html` — Single Jinja2 template for the entire app (two-panel layout: sidebar + main content)
- `static/style.css` — Custom styles including Pygments syntax highlighting theme
- `static/images/` — Images referenced from lesson markdown
- `progress.json` — Auto-created file tracking lesson completion state

## Key Design Decisions

- Single-page layout: sidebar (lesson list + progress) on the left, lesson content on the right
- Full page loads on lesson navigation (no client-side routing needed for localhost)
- Markdown is converted to HTML server-side using Python's `markdown` library with `codehilite` extension
- No authentication, no database, no deployment — local-only
