import os

try:
    SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]
except KeyError:
    raise ValueError("DJANGO_SECRET_KEY environment variable must be set")
