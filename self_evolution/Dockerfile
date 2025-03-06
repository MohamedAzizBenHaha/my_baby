# self_evolution/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN pip install transformers torch numpy requests

# Copy evolution and self-modification scripts
COPY evolve_script.py /app/evolve_script.py
COPY self_modify.py /app/self_modify.py

EXPOSE 5002

CMD ["python", "evolve_script.py"]
