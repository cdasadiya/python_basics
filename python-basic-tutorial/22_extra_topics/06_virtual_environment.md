# Virtual Environment

A virtual environment is an isolated Python workspace for one repository.

## Why it matters

- Keeps project packages separate from your computer's global Python installation.
- Prevents version conflicts between different learning repositories.
- Makes your `requirements.txt` easier to manage.

## Create and activate

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate   # Windows PowerShell
```

## Best practices

- Create one virtual environment per repository.
- Do not commit the `.venv/` folder to GitHub.
- Install packages only after the environment is activated.
