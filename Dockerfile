FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

WORKDIR /app/library

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]