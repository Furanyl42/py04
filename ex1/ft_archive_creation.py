import sys


def ft_archive_creation() -> None:
    lines: list[str] = []
    if len(sys.argv) == 1:
        print(f"Usage: {sys.argv[0]} <file>")
        return
    print("=== Cyber Archives Recovery & Preservation===")
    print(f"Accessing file '{sys.argv[1]}'")
    try:
        f = open(sys.argv[1])
        print("---")
        for line in f:
            clean_line = line.rstrip("\n")
            print(clean_line)
            lines.append(clean_line + "#")
        print("---")
        f.close()
        print(f"File '{sys.argv[1]}' closed.\n")
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError) as e:
        print(f"Error opening file '{sys.argv[1]}': {e}")
        return
    print("Transform data:")
    print("---")
    for line in lines:
        print(line)
    print("---")
    new_file = input("Enter new file name (or empty): ")
    if not new_file:
        print("Not saving data.")
        return

    try:
        f = open(new_file, "w")
        print(f"Saving data to '{new_file}'")
        for l in lines:
            f.writelines(l + "\n")
        f.close()
        print(f"Data saved in file '{new_file}'.")
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError) as e:
        print(f"Error opening file {new_file}: {e}")
        print("Not saving data.")


if __name__ == "__main__":
    ft_archive_creation()
