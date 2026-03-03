# CLAUDE.md

Every time you start a new Claude Code session, it forgets everything from last time. **CLAUDE.md** solves this — it's a file that gets loaded into the context window at the start of every session, giving Claude persistent memory about your project.

## What goes in CLAUDE.md?

Think of it as a README for Claude. Common things to include:

- Your tech stack and frameworks
- How to run, test, and lint the project
- Code conventions and patterns
- Architecture notes and key file paths

## 2 Types of CLAUDE.md

| Scope | Location | Use case |
|-------|----------|----------|
| Project | `CLAUDE.md` or `.claude/CLAUDE.md` | Instructions for this specific project |
| User | `~/.claude/CLAUDE.md` | Personal preferences across all projects |

The project-level file is shared with your team (checked into git). The user-level file is just for you.

> **Tip:** Run `/init` to create a project CLAUDE.md automatically. Claude will scan your codebase and generate a starting point.
