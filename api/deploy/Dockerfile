FROM python:3.7-stretch

WORKDIR /app/code

ADD setup.py /app/code/

ADD skystats /app/code/skystats

RUN ["pip3", "install", "."]

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "skystats.skystats.wsgi"]