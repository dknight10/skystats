from setuptools import setup, find_packages


setup(
    name="skystats-api",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Django",
        "djangorestframework",
        "gunicorn",
        "django-cors-headers",
        "pyexcelerate",
        "djangorestframework-jwt",
        "cryptography",
        "pyjwt",
        "python-dotenv",
        "python-jose",
        "requests",
    ],
    python_requires=">=3.7",
)
