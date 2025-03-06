# web_interface/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN pip install flask

COPY app.py /app/app.py
COPY templates /app/templates

EXPOSE 80

CMD ["python", "app.py"]
