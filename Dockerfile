FROM python:3.8-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY . /app/

RUN pip install -U pip
RUN pip install poetry

RUN poetry config virtualenvs.create false
RUN poetry install --no-root
