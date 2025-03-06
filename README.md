/my_baby
    ├── docker-compose.yml          # Launches the full application
    ├── core_principles.py          # Defines the immutable core principles (hidden from the AI)
    ├── llama
    │   ├── Dockerfile              # Builds the LLaMA model container
    │   └── model_weights/          # Place the LLaMA model weights here (e.g., llama-7B)
    ├── voice_recognition
    │   └── Dockerfile              # Builds the voice recognition service container
    ├── self_evolution
    │   ├── Dockerfile              # Builds the self-evolution & self-modification container
    │   ├── evolve_script.py        # Continuously evolves the AI based on new knowledge
    │   └── self_modify.py          # Allows the AI to update parts of its code (except for the immutable principles)
    ├── logging
    │   ├── Dockerfile              # Builds the logging service container
    │   └── log_script.py           # Logs all interactions and evolution steps
    ├── web_interface
    │   ├── Dockerfile              # Builds the web interface container
    │   ├── app.py                  # Flask web interface for interacting with the AI
    │   └── templates
    │         └── index.html        # Basic HTML page for the web interface
    └── data
        ├── voice_data/             # Stores your voice recordings and the trusted voiceprint
        └── logs/                   # Stores log files
