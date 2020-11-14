FROM python:3.8.6-slim-buster
WORKDIR /usr/src/app/
COPY . /usr/src/app

RUN pip install -r /usr/src/app/requirements.txt
CMD python -u /usr/src/app/app.py
