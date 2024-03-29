FROM python:3.9-slim-buster

ARG POETRY_VERSION=1.1.12

ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN pip install "poetry==$POETRY_VERSION" && poetry config virtualenvs.create false

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry install --no-interaction --no-ansi

CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "nepali_dictionary.main:app", "--reload"]
