# Function to count the number of characters in a file

def count_chars(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            print(f" {len(data)} {file_path}")
    except FileExistsError:
        print(f" File {file_path} not found.")
