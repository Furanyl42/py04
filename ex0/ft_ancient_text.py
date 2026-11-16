import sys


def ft_archive_creation() -> None:
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        f = open(sys.argv[1])
        print("---")
        for line in f:
            print(line.rstrip("\n"))
        print("---")
        f.close()
        print(f"File '{sys.argv[1]}' closed.")
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError) as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return


if __name__ == "__main__":
    ft_archive_creation()
