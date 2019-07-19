FROM python:3.7.4-alpine3.10

WORKDIR /usr/src/app/

COPY . /usr/src/app

VOLUME /usr/src/app/conf

RUN pip install -r /usr/src/app/requirements.txt

CMD python -u /usr/src/app/app.py