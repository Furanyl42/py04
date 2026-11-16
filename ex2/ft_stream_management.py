import sys


def ft_stream_management() -> None:
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
        sys.stdout.flush()
        print(f"[STDERR] Error opening file '{filename}': {e}",
              file=sys.stderr)
        return
    lines: list[str] = []
    try:
        while True:
            line = f.readline()
            if line == "":
                break
            lines.append(line.rstrip("\n"))
    except (OSError, UnicodeDecodeError) as e:
        sys.stdout.flush()
        print(f"[STDERR] Error reading file '{filename}': {e}",
              file=sys.stderr)
        return
    finally:
        f.close()
    print("---")
    for line in lines:
        print(line)
    print("---")
    print(f"File '{filename}' closed.")
    transformed: list[str] = []
    for line in lines:
        transformed.append(line + "#")

    print("Transform data:")
    print("---")
    for line in transformed:
        print(line)
    print("---")
    print("Enter new file name (or empty): ", end="", flush=True)
    new_file = sys.stdin.readline().rstrip("\n")
    if new_file == "":
        print("Not saving data.")
        return
    print(f"Saving data to '{new_file}'")
    sys.stdout.flush()
    try:
        f = open(new_file, "w")
    except (FileNotFoundError, PermissionError, IsADirectoryError,
            OSError) as e:
        print(f"[STDERR] Error opening file '{new_file}': {e}",
              file=sys.stderr)
        print("Data not saved.")
        return
    try:
        for line in transformed:
            f.write(line + "\n")
    except (OSError, UnicodeEncodeError) as e:
        print(f"[STDERR] Error writing file '{new_file}': {e}",
              file=sys.stderr)
        print("Data not saved.")
        return
    finally:
        f.close()
    print(f"Data saved in file '{new_file}'.")


if __name__ == "__main__":
    ft_stream_management()
