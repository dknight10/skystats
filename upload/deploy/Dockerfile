FROM python:3.7-stretch

WORKDIR /app/code

ADD setup.py /app/code/

ADD upload /app/code/upload/

RUN ["pip3", "install", "."]

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "upload.api:app"]