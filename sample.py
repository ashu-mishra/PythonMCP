"""Sample module for PythonMCP repository.

This file provides a tiny example function and a small CLI entry so it's
easy to run and verify the repo contains runnable Python code.
"""

def greet(name: str) -> str:
    """Return a greeting for `name`."""
    return f"Hello, {name}!"


def main() -> None:
    print(greet("World"))


if __name__ == "__main__":
    main()
