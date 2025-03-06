import os

def self_modify():
    """
    Allows the AI to update parts of its own code (except the immutable core principles).
    This is a simple demonstration where the AI appends a comment to a modifiable file.
    """
    modifiable_file = "modifiable_module.py"
    
    # Read current content or initialize if the file doesn't exist.
    if os.path.exists(modifiable_file):
        with open(modifiable_file, "r") as f:
            current_code = f.read()
    else:
        current_code = "# Initial modifiable module\n"
    
    # For demonstration, append a comment.
    new_code = current_code + "\n# Self-modification: Updated by AI during evolution.\n"
    
    # Write updated code back.
    with open(modifiable_file, "w") as f:
        f.write(new_code)
    
    print("Self-modification complete. Updated", modifiable_file)

if __name__ == "__main__":
    self_modify()
