# pip, Package Installation, and Requirements Files

`pip` is Python's package installer. A package is reusable code written by other developers.

## Install one package

```bash
python -m pip install requests
```

## Install all packages from this repository

```bash
python -m pip install -r requirements.txt
```

## Save package versions

```bash
python -m pip freeze > requirements.txt
```

## Best practices

- Prefer `python -m pip` so you use the pip that belongs to the selected Python.
- Keep `requirements.txt` updated when adding packages.
- Read package documentation before using a package in real applications.
