FROM python:3.8.6-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app/

COPY pyproject.toml poetry.lock /app/

RUN apt-get update -y && \
    apt-get install git -y && \
    pip install -U pip && \
    pip install poetry

RUN poetry config virtualenvs.create false && \
    poetry install --no-root

COPY . /app/
