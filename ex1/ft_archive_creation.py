import sys


def ft_archive_creation() -> None:
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
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

    lines: list[str] = []
    for line in content.splitlines():
        lines.append(line + "#")
    print("Transform data:")
    print("---")
    for line in lines:
        print(line)
    print("---")
    new_file = input("Enter new file name (or empty): ")
    if new_file == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_file}'")
    try:
        f = open(new_file, "w")
    except (FileNotFoundError, PermissionError, IsADirectoryError,
            OSError) as e:
        print(f"Error opening file '{new_file}': {e}")
        print("Not saving data.")
        return
    try:
        for line in lines:
            f.write(line + "\n")
    except (OSError, UnicodeEncodeError) as e:
        print(f"Error writing file '{new_file}': {e}")
        print("Not saving data.")
        return
    finally:
        f.close()
    print(f"Data saved in file '{new_file}'.")


if __name__ == "__main__":
    ft_archive_creation()
