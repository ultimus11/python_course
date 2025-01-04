# file_handling.py

# Function to write to a file
def write_to_file(filename, content):
    """Writes content to a file."""
    with open(filename, 'w') as file:
        file.write(content)
    return f"Content written to {filename}"

# Function to read from a file
def read_from_file(filename):
    """Reads content from a file."""
    try:
        with open(filename, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return f"File '{filename}' not found."

# Function to append text to an existing file
def append_to_file(filename, content):
    """Appends content to an existing file."""
    with open(filename, 'a') as file:
        file.write(content)
    return f"Content appended to {filename}"

# Function to read a file line by line
def read_file_line_by_line(filename):
    """Reads a file line by line and returns the lines as a list."""
    try:
        with open(filename, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return f"File '{filename}' not found."

# Function to create a file if it does not exist
def create_file_if_not_exists(filename):
    """Creates an empty file if it does not already exist."""
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write("")
        return f"File '{filename}' created."
    else:
        return f"File '{filename}' already exists."

# Function to read a file and count word frequency
def count_word_frequency(filename):
    """Reads a file and counts the frequency of each word."""
    word_count = {}
    try:
        with open(filename, 'r') as file:
            words = file.read().split()
            for word in words:
                word_count[word] = word_count.get(word, 0) + 1
        return word_count
    except FileNotFoundError:
        return f"File '{filename}' not found."
