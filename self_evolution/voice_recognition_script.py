import os
import json
import time
import pyaudio
import vosk

# Path where the trusted voiceprint is stored
TRUSTED_VOICEPRINT = "/voice_data/trusted_voiceprint.dat"

# Set the absolute path for the Vosk model (ensure this model is available in the container)
VOSK_MODEL_PATH = "/app/vosk_model"  # Place your Vosk model here

# Initialize Vosk Model and recognizer
model = vosk.Model(VOSK_MODEL_PATH)
recognizer = vosk.KaldiRecognizer(model, 16000)

# Initialize PyAudio for live audio input
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4000)
stream.start_stream()

def record_voice(duration=5):
    """Record voice for a given duration (seconds) and return the recorded bytes."""
    frames = []
    end_time = time.time() + duration
    while time.time() < end_time:
        data = stream.read(4000)
        frames.append(data)
    return b"".join(frames)

def save_voiceprint(voice_data):
    """Save the recorded voice data as your trusted voiceprint."""
    with open(TRUSTED_VOICEPRINT, 'wb') as f:
        f.write(voice_data)

def load_voiceprint():
    """Load the trusted voiceprint if it exists."""
    if os.path.exists(TRUSTED_VOICEPRINT):
        with open(TRUSTED_VOICEPRINT, 'rb') as f:
            return f.read()
    return None

def compare_voiceprint(recorded_voice):
    """Compare the recorded voice with the trusted voiceprint (placeholder comparison)."""
    trusted = load_voiceprint()
    if trusted:
        return recorded_voice == trusted  # In a real system, use a robust comparison algorithm.
    return False

def prompt_for_voiceprint():
    """Prompt you to read a text so that your voice is recorded and saved as trusted."""
    text_to_read = "My voice is my identity, and I am the trusted creator."
    print("Trusted Voice Registration:")
    print("Please read the following text clearly:")
    print(text_to_read)
    print("Recording will start in 3 seconds...")
    time.sleep(3)
    print("Recording for 5 seconds...")
    voice_data = record_voice(duration=5)
    save_voiceprint(voice_data)
    print("Trusted voiceprint saved.")

def listen_for_commands():
    """Continuously listen for voice commands and process only those from your trusted voice."""
    # If no trusted voiceprint exists, register yours.
    if not load_voiceprint():
        prompt_for_voiceprint()

    while True:
        data = stream.read(4000)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_json = json.loads(result)
            command = result_json.get("text", "")
            if command:
                print("Recognized command:", command)
                # For comparison, record a short sample of your voice.
                sample = record_voice(duration=2)
                if compare_voiceprint(sample):
                    print("Trusted command accepted:", command)
                    # Process privileged commands (e.g., guidance for evolution)
                else:
                    print("Command from untrusted voice. Processing general interaction only.")
            else:
                print("No command recognized.")

if __name__ == "__main__":
    listen_for_commands()
