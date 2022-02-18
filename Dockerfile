FROM python:3.9.7-slim-buster

ADD ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

ADD . /app

WORKDIR /app

CMD ["python3", "app.py"]