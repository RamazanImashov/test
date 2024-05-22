FROM python:3.11

WORKDIR /project

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY . .

RUN pip install --upgrade pip

RUN pip install -r req.txt