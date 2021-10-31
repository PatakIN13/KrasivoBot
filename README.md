# Install / Установить
Please, always install your app dependencies inside `virtualenv`.  
Пожалуйста, всегда устанавливайте зависимости вашего приложения внутри `virtualenv`.
```
python -m venv venv
. venv/bin/activate
pip install -r requirements.txt
```

# Run / Запустить
```
TELEGRAM_TOKEN=123-c00l-t0k3n python -m krasivo_bot
```

# Develop
```
pip install -r requirements.txt -r requirements-dev.txt
```

# Lint
`pre-commit` will run all the hooks described in `.pre-commit-config.yaml` on each commit or you can check all files manually   
`pre-commit` будет запускать все хуки, описанные в` .pre-commit-config.yaml` при каждой фиксации, или вы можете проверить все файлы вручную:
```
pre-commit run --all-files
```
Since `mypy` needs all dependencies to resolve imports, run it manually   
Поскольку `mypy` нужны все зависимости для разрешения импорта, запустите его вручную:
```
mypy --install-types krasivo_bot
```