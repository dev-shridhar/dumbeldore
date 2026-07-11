# tests/

Unit tests for the Dumbledore bot.

Run all tests:
```bash
pytest tests/ -v
```

- `test_brain.py` — Prompt loading and message building
- `test_llm.py` — Ollama/Groq fallback logic
- `test_memory.py` — Group memory buffer
- `conftest.py` — sys.path setup for imports
