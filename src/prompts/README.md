# prompts/

Versioned prompt templates for the bot's LLM responses.

Each prompt type has its own file with a version suffix (e.g., `challenge_v1.py`).

When adding or updating prompts:
1. Create new file with incremented version
2. Update `__init__.py` VERSION and mappings
3. Keep old versions for backward compatibility
