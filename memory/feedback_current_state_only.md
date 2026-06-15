# Instruction Files — Current State Only

When editing CLAUDE.md, REQUIREMENTS.md, or any project instruction file, write only the current state. Do not add parenthetical history notes like "(the primary deliverable — no solutions.md)" or "was previously X". Instruction files are not a changelog.

**Why:** Adding old-decision context leaves stale information that contradicts itself as the project evolves, making the files harder to trust.

**How to apply:** If you change a file role or convention, update the file to state the new fact cleanly. Record the reason for the change in the git commit message only, not in the instruction file.
