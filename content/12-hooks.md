# Hooks

Hooks let you automate actions before and after tool calls. Every time Claude uses a tool (reading a file, running a command, etc.), you can run your own code at two points: **before** the tool executes and **after** it finishes.

## The flow

Without hooks: **Calls Tool → Tool Execution → Tool Result**

With hooks: **Calls Tool → Pre-tool Hook → Tool Execution → Post-tool Hook → Tool Result**

## Creating a hook

Hooks are defined in `settings.json`:

```json
{
  "hooks": {
    "HookTrigger": [
      {
        "matcher": "Tool name or regex pattern",
        "hooks": [
          {
            "type": "command",
            "command": "shell command to run"
          }
        ]
      }
    ]
  }
}
```

## 2 Hook Scopes

| Scope | Location |
|-------|----------|
| Project | `.claude/settings.json` |
| User | `~/.claude/settings.json` |

## More options

- **More triggers:** SessionStart, Notification, and more
- **More hook types:** Command, Prompt, Agent, HTTP

## References

- [Claude Code in Action (course)](https://anthropic.skilljar.com/claude-code-in-action)
- [Hooks Guide](https://code.claude.com/docs/en/hooks-guide)
