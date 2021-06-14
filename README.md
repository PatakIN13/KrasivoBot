# Install
Please, always install your app dependencies inside `virtualenv`.
```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

# Run
```
TELEGRAM_TOKEN=123-c00l-t0k3n python -m krasivo_bot
```

# Develop
```
pip install -r requirements.txt -r requirements-dev.txt
```

# Lint
`pre-commit` will run all the hooks described in `.pre-commit-config.yaml` on each commit or you can check all files manually:
```
pre-commit run --all-files
```
Since `mypy` needs all dependencies to resolve imports, run it manually:
```
mypy --install-types krasivo_bot
```