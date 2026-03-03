# Basic Usage

There are three things to know when using Claude Code day-to-day: **modes**, **tagging**, and **undoing stuff**.

## 1) Modes

Claude Code has two modes you can toggle with `Shift + Tab`:

- **Chat mode** (default) — Claude can read and write files freely. The status bar shows `accept edits on`.
- **Plan mode** — Claude researches and plans but won't make changes until you approve. The status bar shows `plan mode on`.

**When to use Plan mode:** Start with plan mode for complex tasks. Let Claude explore the codebase and propose an approach before making edits.

## 2) Tag files and folders

You can point Claude to specific files or folders by tagging them in your message:

- `@file.py` — adds a specific file to Claude's context
- `@folder/` — adds an entire folder

This saves tokens because Claude doesn't have to search for the files itself.

## 3) Undo stuff

Made a mistake? You have two escape hatches:

- **ESC** — Clear your current message
- **ESC ESC** (double tap) — Restore your code and conversation to a previous state. Use this when Claude goes down a wrong path.
