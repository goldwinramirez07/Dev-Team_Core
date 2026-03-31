import os

def read_file(path):
    with open(path, "r") as f:
        return f.read()

def write_file(path, content):
    # Create folder if it doesn't exist
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w") as f:
        f.write(content)