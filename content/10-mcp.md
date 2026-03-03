# MCP

MCP (Model Context Protocol) is a universal way to give Claude access to external tools and context. It connects Claude to things like GitHub, databases, Google Drive, Slack, Notion, and more.

## What is an MCP server?

An MCP server is a small program that exposes tools to Claude. For example, a GitHub MCP server might give Claude tools to create PRs, read issues, and manage repos.

## Adding an MCP server

```bash
# Basic syntax
claude mcp add --transport http <name> <url>
```

Use `--scope` to control where it's available: `local`, `project`, or `user`.

## 3 MCP Server Scopes

| Scope | Location | Shared? |
|-------|----------|---------|
| Project | `.mcp.json` | Yes (checked into git) |
| User | `~/.claude.json` | No (personal) |
| Local | `~/.claude.json` | No (project-level, not shared) |

MCP servers let you connect Claude to basically any app or service. If there's an API, there's probably an MCP server for it.

## References

- [MCP Deep Dive (video)](https://youtu.be/N3vHJcHBS-w)
