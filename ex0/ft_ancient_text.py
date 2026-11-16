import sys


def ft_ancient_text() -> None:
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file '{filename}'")
    try:
        f = open(filename)
    except (FileNotFoundError, PermissionError, IsADirectoryError,
            OSError) as e:
        print(f"Error opening file '{filename}': {e}")
        return
    try:
        content = f.read()
    except (OSError, UnicodeDecodeError) as e:
        print(f"Error reading file '{filename}': {e}")
        return
    finally:
        f.close()
    print("---")
    print(content, end="")
    if content != "" and not content.endswith("\n"):
        print()
    print("---")
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    ft_ancient_text()
