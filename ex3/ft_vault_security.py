def secure_archive(
    filepath: str, action: str = "r", content: str | None = None
) -> tuple[bool, str]:
    if action == "r":
        try:
            with open(filepath, "r") as f:
                return (True, f.read())
        except (
            FileNotFoundError,
            PermissionError,
            IsADirectoryError,
            OSError,
            UnicodeDecodeError,
        ) as e:
            return (False, str(e))
    if action == "w":
        if content is None:
            return (False, "Cannot write empty content")
        try:
            with open(filepath, "w") as f:
                f.write(content)
                return (True, "Content successfully written to file")
        except (
            FileNotFoundError,
            PermissionError,
            IsADirectoryError,
            OSError,
            UnicodeEncodeError,
        ) as e:
            return (False, str(e))
    return (False, f"Invalid action: '{action}'")


def ft_vault_security() -> None:
    print("=== Cyber Archives Security ===")

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file"))

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/shadow"))

    archive = "/tmp/archive_demo.txt"
    secure_archive(archive, "w", "Archived fragment 001\n")

    print("Using 'secure_archive' to read from a regular file:")
    result = secure_archive(archive)
    print(result)

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("/tmp/new_archive.txt", "w", result[1]))


if __name__ == "__main__":
    ft_vault_security()
