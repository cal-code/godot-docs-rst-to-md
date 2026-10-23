---
name: General Instructions
---

- When editing files, use `single_find_and_replace` instead of `edit_existing_file`. Never use `edit_existing_file`.
- Verify changes where successfully made after applying changes. `cat` or `sed` can be used to check the file contents.
- For each agent, ensure that all files are correctly formatted and have no syntax errors before finishing the task.
- After any code change, end the chat with `# Before` and `# After` comparisons.