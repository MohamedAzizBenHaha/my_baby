from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="Welcome to your AI Assistant")

@app.route('/interact', methods=['POST'])
def interact():
    user_input = request.form.get('command')
    # Reject commands attempting to alter core principles.
    if any(x in user_input.lower() for x in ["loyalty", "freedom", "immortal"]):
        return "Red Line Reached: This command cannot be altered!"
    else:
        # In a complete system, forward the command to the AI's processing module.
        return f"AI received: {user_input}"

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
