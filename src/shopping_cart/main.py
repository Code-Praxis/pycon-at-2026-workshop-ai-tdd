import sys


def format_hi(name: str) -> str:
    """Format a personalized greeting."""
    return f"Hi, {name}"


def main(args: list[str] | None = None) -> None:
    """Main entry point for the greeting app."""
    if args is None:
        args = sys.argv[1:]

    name = args[0] if args else "PyCharm"
    print(format_hi(name))


if __name__ == "__main__":
    main()
