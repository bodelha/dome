FROM python:3.12-alpine

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml pyproject.toml
COPY poetry.lock poetry.lock

RUN poetry config virtualenvs.create false
RUN poetry install --no-dev

COPY . .

EXPOSE 5000

CMD ["poetry", "run", "python", "app.py"]