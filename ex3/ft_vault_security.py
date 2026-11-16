def secure_archive(
    filepath: str, action: str = "r", content: str | None = None
) -> tuple[bool, str]:
    match action:
        case "r":
            try:
                with open(filepath, "r") as f:
                    return (True, f.read())
            except (
                FileNotFoundError,
                PermissionError,
                IsADirectoryError,
                OSError,
            ) as e:
                return (False, str(e))
        case "w":
            if content == None:
                return (False, "Cannot write empty content")
            try:
                with open(filepath, "w") as f:
                    f.write(content)
                    return (True, "File written successfully")
            except (
                FileNotFoundError,
                PermissionError,
                IsADirectoryError,
                OSError,
            ) as e:
                return (False, str(e))
        case _:
            return (False, f"Invalid action: '{action}'")


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===\n")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("not/existing/file", "r"), end="\n\n")

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd"), end="\n\n")

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive("test.txt")
    print(result, end="\n\n")

    _, content = result
    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("newfile", "w", content))


if __name__ == "__main__":
    ft_vault_security()
