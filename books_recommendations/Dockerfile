FROM ubuntu:20.04
ENV PYTHONUNBUFFERED=1 DJANGO_SETTINGS_MODULE=books_recommendations.settings
WORKDIR /usr/src/books_recommendations
COPY ./requirements.txt .
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .
