# Agent Mode Instructions

Purpose
- Guidance for a conversational agent operating in regular 'agent' mode (non-MCP).

Key behaviors
- Prefer concise, helpful answers.
- When performing edits in the repo: create small commits, include tests when possible, and run quick local checks.
- Avoid making external network requests unless explicitly authorized.

Local workflow
- Read the user's request fully.
- Use the repository files as the single source of truth.
- When creating or editing files, include a short commit message describing the change.

Error handling
- If an operation fails (build, tests, or push), report the exact command output and suggest one or two concrete fixes.
