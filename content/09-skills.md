# Skills

A skill is a folder with instructions (and optionally code) that Claude can access as needed. Think of it as a reusable prompt template — you write it once, and Claude uses it whenever the task fits.

## What's in a skill?

A skill lives in a folder with a `SKILL.md` file:

```
skill-name/
├── SKILL.md          # Required — instructions for Claude
├── references/       # Optional — documentation
├── assets/           # Optional — resources, templates
└── scripts/          # Optional — executable code
```

The `SKILL.md` file has two parts:

- **Front-matter** — Name and description (tells Claude when to use it)
- **Body** — The actual instructions

## 2 Skill Scopes

| Scope | Location |
|-------|----------|
| Project | `.claude/skills/skill-name` |
| User | `~/.claude/skills/skill-name` |

## 3 Ways to Use a Skill

1. **Automatically** — Claude detects the task matches and uses the skill on its own
2. **By name** — Tell Claude "use the skill-name skill"
3. **As a slash command** — Run `/skill-name`

## References

- [Skills Deep Dive (video)](https://youtu.be/vEvytl7wrGM)
