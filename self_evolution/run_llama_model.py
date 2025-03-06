from transformers import pipeline

# Load LLaMA model (assumes weights are in /model_weights/llama-7B)
model = pipeline('text-generation', model='/model_weights/llama-7B')

def generate_response(prompt):
    response = model(prompt)
    return response[0]['generated_text']

if __name__ == "__main__":
    prompt = "Hello, what is your name?"
    print("AI Response:", generate_response(prompt))
