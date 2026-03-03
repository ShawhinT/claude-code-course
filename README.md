# Claude Code Crash Course

A local-only, single-page web app for learning Claude Code. Clone the repo, run it locally, and follow along with the course content.

Resources:
- [Video Explainer]

## Getting Started

```bash
# Install dependencies
uv sync

# Start the dev server
uv run uvicorn app:app --reload --port 8000

# Open in browser
open http://127.0.0.1:8000
```

## Tech Stack

- Python 3.13 + UV
- FastAPI + Jinja2 + Uvicorn
- Tailwind CSS (CDN)
- Markdown + Pygments for syntax highlighting

## License

Apache 2.0
