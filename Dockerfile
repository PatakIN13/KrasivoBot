FROM python:3.12-alpine

WORKDIR /bot

COPY . /bot

RUN pip install --no-cache-dir poetry
RUN poetry config virtualenvs.create false
RUN poetry install

CMD ["sh", "-c", "poetry run python -m krasivo_bot"]