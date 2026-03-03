# Slash Commands

Slash commands are shortcuts for common Claude Code actions. Type `/` followed by the command name.

## Key commands

**`/context`** — See how your context window is being used. Shows a breakdown of tokens by category (system prompt, tools, messages, free space). Useful for knowing when you're running low.

**`/clear`** — Wipe the conversation history and start fresh. Use this when you're switching to a new task and want a clean slate.

**`/compact`** — Clear the conversation history, but keep a summary. This is the best of both worlds — you free up space while Claude still remembers what you've been working on.

## How `/compact` works

When you run `/compact`, the context window goes from being full of messages to containing just:

1. System Message
2. Tools
3. CLAUDE.md
4. **Conversation summary** (a compressed version of everything so far)

This gives you a fresh context window without losing the thread.

> **Tip:** Run `/help` to see all available slash commands.
