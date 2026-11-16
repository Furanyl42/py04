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
        print(f"[STDERR] Error opening file '{sys.argv[1]}': {e}", file=sys.stderr)
        return
    print("Transform data:")
    print("---")
    for line in lines:
        print(line)
    print("---")
    print("Enter new file name (or empty): ", end="", flush=True)
    new_file = sys.stdin.readline().rstrip("\n")
    if not new_file:
        print("Not saving data.")
        return
    try:
        f = open(new_file, "w")
        for l in lines:
            f.writelines(l + "\n")
        f.close()
        print(f"Data saved in file '{new_file}'")
    except (FileNotFoundError, PermissionError, IsADirectoryError, OSError) as e:
        print(f"[STDERR] Error opening file {new_file}: {e}", file=sys.stderr)
        print("[STDERR] Not saving data.", file=sys.stderr)


if __name__ == "__main__":
    ft_archive_creation()
