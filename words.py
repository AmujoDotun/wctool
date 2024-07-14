#function to count the numner of words in a file

def count_words(file_path):
    try:
        with open(file_path, 'r') as file:
            words = file.read().split()
            print(f" {len(words)} {file_path}")
    except FileExistsError:
        print(f" File {file_path} not found")