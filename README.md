# Установить
Пожалуйста, всегда устанавливайте зависимости вашего приложения внутри `virtualenv`.
```bash
python -m venv venv
. venv/bin/activate
pip install poetry
poetry install
```
# Запустить
## ENV
Создайте переменую окружения в файле `.env`:
```env
TELEGRAM_TOKEN=BOT_TOKEN
```
## Запуск
```bash
poetry run python -m krasivo_bot
```
