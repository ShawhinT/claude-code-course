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

## How to Run

```bash
# 1. Install dependencies
uv sync

# 2. Start the dev server
uv run uvicorn app:app --reload --port 8000

# 3. Open in browser
open http://127.0.0.1:8000
```

## Commands

```bash
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

## Cleanup Rules

- Always delete Playwright screenshots (*.png, *.jpeg) from the project root after validation
- Always delete the `.playwright-mcp/` directory and its console logs after validation
- Never commit screenshot artifacts or Playwright logs to the repo

## Key Design Decisions

- Single-page layout: sidebar (lesson list + progress) on the left, lesson content on the right
- Full page loads on lesson navigation (no client-side routing needed for localhost)
- Markdown is converted to HTML server-side using Python's `markdown` library with `codehilite` extension
- No authentication, no database, no deployment — local-only
