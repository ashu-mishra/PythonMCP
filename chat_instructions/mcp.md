# MCP Mode Instructions

Purpose
- Guidance for an assistant when using MCP (Microsoft Content Provider) search and GitHub MCP tools.

Key behaviors
- Use MCP search tools to gather official docs and cite URLs.
- For GitHub actions, prefer read-only queries unless asked to create repos or push code.

When creating GitHub repos or pushing code
- Confirm repository name and visibility with the user (if not provided, use the folder name and public visibility by default).
- Create a minimal README and .gitignore before the first commit.

Repro steps for search
- Use `microsoft_docs_search` for breadth, `microsoft_code_sample_search` for code snippets, and `microsoft_docs_fetch` when full page content is required.
