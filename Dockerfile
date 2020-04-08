FROM python:3.6.8

RUN mkdir /app && python -m pip install -U pip

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV DJANGO_SETTINGS_MODULE kvdomingo.settings

COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

CMD python manage.py runserver 0.0.0.0:8000
