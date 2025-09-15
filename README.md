
# Works Out Of The Box — 2025-09-15

Upload *the contents* of this zip to a new or existing GitHub repo. That's it.
- CI is enabled via `.github/workflows/ci.yml`
- `main.py` logs to `ledger.txt`
- `tests/` has a smoke test

## Optional: run locally
```
python main.py did a thing
python -m unittest discover -s tests
```
