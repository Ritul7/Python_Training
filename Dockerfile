FROM python:3.12-slim

WORKDIR /myproject

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["python3", "manage.py", "runserver"]
