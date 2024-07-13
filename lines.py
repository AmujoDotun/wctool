#Function to count lines

def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            print(f" {len(lines)} {file_path}")
    except FileExistsError:
        print(f"File {file_path} not found.")