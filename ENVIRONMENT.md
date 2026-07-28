# Environment

## Python version

Use Python 3.10 or newer.

## Recommended setup

Create a project-local virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

On macOS or Linux, activate it with:

```bash
source .venv/bin/activate
```

If you prefer Conda:

```powershell
conda create -n ml-katas python=3.11
conda activate ml-katas
python -m pip install -r requirements.txt
```

Verify the interpreter:

```powershell
python -c "import sys; print(sys.version); print(sys.executable)"
```

## Optional package mirror

When PyPI access is slow in mainland China, supply a mirror explicitly:

```powershell
python -m pip install -r requirements.txt `
  -i https://pypi.tuna.tsinghua.edu.cn/simple
```

## Command rules

1. Activate one environment before running tests or scripts.
2. Confirm `sys.executable` when the active environment is uncertain.
3. Install packages only after confirming they are necessary.
4. Record new runtime or test dependencies in `requirements.txt`.
5. Do not commit `.venv/`, caches, credentials, or machine-specific configuration.
