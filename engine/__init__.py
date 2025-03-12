import os

def create_empty_file(filepath):
  """Creates an empty file at the specified filepath.

  Args:
    filepath: The path to the file to be created.
  """
  try:
    with open(filepath, 'w') as f:
      pass  # 'pass' does nothing, effectively creating an empty file
    print(f"File '{filepath}' created successfully.")
  except Exception as e:
    print(f"An error occurred: {e}")

# Example usage (creates a file named 'my_empty_file.txt'):
create_empty_file("my_empty_file.txt")