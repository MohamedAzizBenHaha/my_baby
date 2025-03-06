# llama/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN pip install torch transformers

# Copy model weights (place your LLaMA weights here later)
COPY ./model_weights /model_weights

# Copy the LLaMA model script from self_evolution (shared script)
COPY ../self_evolution/run_llama_model.py /app/run_llama_model.py

EXPOSE 5000

CMD ["python", "run_llama_model.py"]
