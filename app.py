import json
from pathlib import Path

import markdown
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
CONTENT_DIR = BASE_DIR / "content"
PROGRESS_FILE = BASE_DIR / "progress.json"

app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=BASE_DIR / "templates")


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def _extract_title(path: Path, fallback: str) -> str:
    """Extract the H1 title from a markdown file, or use the fallback."""
    for line in path.read_text().splitlines():
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return fallback


def get_lessons() -> list[dict]:
    """Scan content/*.md, sort by numeric prefix, return lesson metadata."""
    lessons = []
    if not CONTENT_DIR.exists():
        return lessons
    for path in sorted(CONTENT_DIR.glob("*.md")):
        stem = path.stem  # e.g. "01-what-is-claude-code"
        parts = stem.split("-", 1)
        if len(parts) == 2 and parts[0].isdigit():
            order = int(parts[0])
            fallback_title = parts[1].replace("-", " ").title()
        else:
            order = 0
            fallback_title = stem.replace("-", " ").title()
        title = _extract_title(path, fallback_title)
        lessons.append(
            {
                "slug": stem,
                "title": title,
                "order": order,
                "path": path,
            }
        )
    return lessons


def read_progress() -> dict:
    """Read progress.json, returning an empty dict if the file doesn't exist."""
    if not PROGRESS_FILE.exists():
        return {}
    try:
        return json.loads(PROGRESS_FILE.read_text())
    except (json.JSONDecodeError, OSError):
        return {}


def write_progress(data: dict) -> None:
    """Write progress data to progress.json."""
    PROGRESS_FILE.write_text(json.dumps(data, indent=2))


def render_markdown(path: Path) -> str:
    """Convert a markdown file to HTML with syntax highlighting and tables."""
    md = markdown.Markdown(
        extensions=["codehilite", "fenced_code", "tables"],
        extension_configs={
            "codehilite": {
                "css_class": "codehilite",
                "guess_lang": False,
            }
        },
    )
    return md.convert(path.read_text())


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------


@app.get("/")
def home():
    """Redirect to the first lesson, or return a simple message if none exist."""
    lessons = get_lessons()
    if not lessons:
        return RedirectResponse(url="/")
    return RedirectResponse(url=f"/lesson/{lessons[0]['slug']}")


@app.get("/lesson/{slug}")
def lesson(request: Request, slug: str):
    """Render a single lesson page with sidebar navigation and progress."""
    lessons = get_lessons()
    if not lessons:
        return RedirectResponse(url="/")

    # Find the current lesson by slug
    current_lesson = None
    current_index = None
    for i, item in enumerate(lessons):
        if item["slug"] == slug:
            current_lesson = item
            current_index = i
            break

    if current_lesson is None:
        return RedirectResponse(url="/")

    # Render markdown to HTML
    content_html = render_markdown(current_lesson["path"])

    # Previous / next lessons
    prev_lesson = lessons[current_index - 1] if current_index > 0 else None
    next_lesson = (
        lessons[current_index + 1] if current_index < len(lessons) - 1 else None
    )

    # Progress tracking
    progress = read_progress()
    is_completed = progress.get(slug, False)
    completed_count = sum(1 for item in lessons if progress.get(item["slug"], False))
    total_count = len(lessons)
    progress_pct = int((completed_count / total_count) * 100) if total_count else 0

    # Build sidebar lesson list with active/completed flags
    lesson_list = [
        {
            **item,
            "completed": progress.get(item["slug"], False),
            "active": item["slug"] == slug,
        }
        for item in lessons
    ]

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "lessons": lesson_list,
            "current_lesson": current_lesson,
            "content_html": content_html,
            "prev_lesson": prev_lesson,
            "next_lesson": next_lesson,
            "is_completed": is_completed,
            "progress_pct": progress_pct,
            "completed_count": completed_count,
            "total_count": total_count,
        },
    )


@app.post("/progress/{slug}")
def complete_and_next(slug: str, next: str = ""):
    """Mark lesson as complete and redirect to the next lesson."""
    progress = read_progress()
    progress[slug] = True
    write_progress(progress)
    redirect_to = f"/lesson/{next}" if next else f"/lesson/{slug}"
    return RedirectResponse(url=redirect_to, status_code=303)
