FROM python:3.8.3-alpine

# set work directory
RUN mkdir -p /srv/app
WORKDIR /srv/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /srv/app

RUN apk add --update --virtual .build-deps \
        g++ \
        python3-dev \
        libxml2 \
        libxml2-dev && \
    apk add libxslt-dev

RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

RUN apk del .build-deps

# copy project
COPY . /srv/app

# CMD gunicorn -w 2 -t 180 app.wsgi:application --bind 0.0.0.0:$PORT
EXPOSE 8000