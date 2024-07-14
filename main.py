import sys
from countbytes import count_bytes
from lines import count_lines
from characters import count_chars

if __name__ == "__main__":
    print(f"Arguments received: {sys.argv}")
    if len(sys.argv) != 3 or sys.argv[1] not in ['-c', '-l']:
        print("Usage: main.py -c <file> or main.py -l <file>")
    else:
        option = sys.argv[1]
        file_path = sys.argv[2]
        print(f"Option selected: {option}")
        print(f"File path: {file_path}")

        if option == '-c':
            count_bytes(file_path)
        elif option == '-l':
            count_lines(file_path)
