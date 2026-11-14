from importlib.metadata import version

def main() -> None:
    print(f"mcarchive-api-python v{version("wheel")}")
