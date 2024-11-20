FROM python:3.12-alpine

WORKDIR /app

RUN pip install poetry

COPY ./api/pyproject.toml ./api/poetry.lock ./

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY ./api /app/api
COPY ./docs /app/docs

EXPOSE 5000

CMD ["poetry", "run", "python", "api/app.py"]
