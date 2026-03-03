# Subagents

Subagents let Claude outsource work to fresh, specialized agents. Each subagent gets its own context window, so the main conversation doesn't get cluttered with intermediate work.

## Built-in subagents

- **Explore** — Uses Haiku (fast, cheap), read-only tools. Best for file discovery and code search.
- **Plan** — Same model as main, read-only tools. Best for codebase research and planning.
- **General-purpose** — Same model as main, all tools. Best for complex research and operations.

## Custom subagents

You can create your own subagents with a markdown file:

```yaml
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. When invoked, analyze the code and provide
specific, actionable feedback on quality, security, and best practices.
```

## 2 Subagent Scopes

| Scope | Location |
|-------|----------|
| Project | `.claude/agents/` |
| User | `~/.claude/agents/` |

## References

- [Subagents Documentation](https://code.claude.com/docs/en/sub-agents)
