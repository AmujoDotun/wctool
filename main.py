

if __name__ == "__main__ ":
    if len(sys.argv) != 3 or sys.argv[1] not in ['-c', '-l']:
        print("Usage: ccwc -c <file> or ccwc -l <file>")
    elif sys.argv[1] == '-c':
        count_bytes(sys.argv[2])
    elif sys.argv[1] == '-l':
        count_lines(sys.argv[2])