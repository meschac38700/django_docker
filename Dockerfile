FROM python:3.9

COPY requirements.txt .

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . .

EXPOSE 80/tcp

CMD ["python", "manage.py", "runserver", "0.0.0.0:80"]
