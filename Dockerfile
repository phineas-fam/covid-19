FROM python:3.8.1-slim-buster

WORKDIR /app

ENV FLASK_DEBUG=True
ENV FLASK_APP=covidbe.main

COPY requirements.txt ./
COPY . /app
RUN pip install --no-cache -r requirements.txt

EXPOSE 5002

CMD ["gunicorn",  "--bind=0.0.0.0:5000", "covidbe.main:app"]
