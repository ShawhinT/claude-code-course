# What is Claude Code?

Claude Code is an AI agent that can build software. It's not just a chatbot that answers questions — it's an agent that can actually read your files, run commands, search the web, and write code on your behalf.

## What makes it an "agent"?

A regular AI chatbot takes your message and gives a response. An agent goes further — it has **tools**. Claude Code combines Claude (the AI model) with a set of tools, and that combination is what makes it an agent.

## What tools does Claude Code have?

Claude Code's toolset changes frequently, so if you're ever unsure, just ask Claude! Here's a summary of the current tools.

| Category | Tool | Description |
|----------|------|-------------|
| File Operations | Read | Read files from the filesystem |
| | Write | Write/create files |
| | Edit | Make precise string replacements in files |
| | NotebookEdit | Edit Jupyter notebook cells |
| | Glob | Find files by pattern matching |
| | Grep | Search file contents with regex |
| Execution | Bash | Run shell commands |
| Web | WebFetch | Fetch and analyze content from a URL |
| | WebSearch | Search the web |
| Agents & Tasks | Agent | Launch specialized subagents |
| | TaskCreate | Create tasks in a task list |
| | TaskGet | Retrieve a task by ID |
| | TaskUpdate | Update task status or details |
| | TaskList | List all tasks |
| | TaskOutput | Get output from a background task |
| | TaskStop | Stop a running background task |
| Workflow | Skill | Invoke user-defined skills (e.g. `/commit`) |
| | EnterPlanMode | Plan before building |
| | ExitPlanMode | Exit plan mode and request approval |
| | EnterWorktree | Create an isolated git worktree |
| | AskUserQuestion | Ask the user clarifying questions |
