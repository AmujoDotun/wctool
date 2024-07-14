import sys
from countbytes import count_bytes
from lines import count_lines
from characters import count_chars

if __name__ == "__main__":
    print(f"Arguments received: {sys.argv}")
    if len(sys.argv) != 3 or sys.argv[1] not in ['-c', '-l', '-w', '-m']:
        print("Usage: main.py -c <file>, main.py -l <file>, main.py -w <file>, main.py -m <file>")
    elif sys.argv[1] == '-c':
        count_bytes(sys.argv[2])
    elif sys.argv[1] == '-l':
        count_lines(sys.argv[2])
    elif sys.argv[1] == '-w':
        count_words(sys.argv[2])
    elif sys.argv[1] == '-m':
        count_chars(sys.argv[2])