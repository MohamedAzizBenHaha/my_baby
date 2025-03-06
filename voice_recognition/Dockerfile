# voice_recognition/Dockerfile

FROM python:3.9-slim

WORKDIR /app

RUN pip install vosk pyaudio numpy

# Copy the voice recognition script from self_evolution (shared script)
COPY ../self_evolution/voice_recognition_script.py /app/voice_recognition_script.py

EXPOSE 5001

CMD ["python", "voice_recognition_script.py"]
