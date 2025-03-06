import logging

logging.basicConfig(filename='/logs/ai_interactions.log', level=logging.INFO,
                    format='%(asctime)s %(levelname)s:%(message)s')

def log_interaction(command, status):
    logging.info(f"Command: {command} | Status: {status}")

if __name__ == "__main__":
    log_interaction("System startup", "OK")
    print("Logging service running...")
