# My first file tracked by Git
# Author: Albert Hernansanz

def greet(name):
    """Return a welcome message for the given name."""
    return f"Hello, {name}! Welcome to Git."

def farewell(name):
    """Return a goodbye message for the given name."""
    return f"Goodbye, {name}! See you next commit."

# This block runs only when the file is executed directly,
# not when it is imported as a module from another file.
if __name__ == "__main__":
    print(greet("World"))     # Call the greet function and print the result
    print(farewell("World"))  # Call the farewell function and print the result