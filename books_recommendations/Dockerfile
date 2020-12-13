FROM python:3.8.3-alpine
ENV PYTHONUNBUFFERED=1 DJANGO_SETTINGS_MODULE=books_recommendations.settings
WORKDIR /usr/src/books_recommendations
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .