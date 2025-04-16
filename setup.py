from setuptools import setup, find_packages

setup(
    name="research-journal",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "Django==4.2.9",
        "Pillow==10.2.0",
        "python-dotenv==1.0.0",
        "django-crispy-forms==2.0",
        "crispy-bootstrap5==0.7",
        "django-taggit==4.0.0",
        "whitenoise==6.5.0",
        "gunicorn==21.2.0",
        "dj-database-url==0.5.0",
        "psycopg2-binary==2.9.9",
        "python-memcached==1.59",
        "boto3==1.34.7",
        "botocore==1.34.7",
        "psycopg2==2.9.9",
        "Pillow-SIMD==9.5.1",
        "sqlparse==0.5.3",
        "tzdata==2025.2",
        "asgiref==3.8.1"
    ],
    python_requires='>=3.11',
)
