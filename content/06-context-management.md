# Context Management

Claude Code has a **context window** — a limited amount of information it can hold at once. Managing it well is the key to getting good results.

## What's in the context window?

Every time you send a message, the context window contains:

1. **System Message** — Claude's built-in instructions
2. **Tools** — Descriptions of all available tools
3. **CLAUDE.md** — Your project instructions (more on this next)
4. **Your Request** — What you just asked
5. **Extended Thinking** — Claude's reasoning
6. **Tool Calls & Results** — Files read, commands run, etc.
7. **Response** — Claude's answer

As the conversation grows, all of this accumulates and eats into the available space.

## Tips for managing context

- **Start with Plan mode** — Let Claude research first, then switch to execution. This avoids wasted tokens on wrong approaches.
- **Tag files with @** — Point Claude directly at files so it doesn't waste tokens searching for them.
- **Double ESC to rewind** — If Claude goes on a tangent (brainstorming, arguing, making mistakes), double-tap ESC to roll back and try again.

## References

- [Context Window Deep Dive (video)](https://youtu.be/PCLu84VLF1w)
- [Claude Code in Action (course)](https://anthropic.skilljar.com/claude-code-in-action)
