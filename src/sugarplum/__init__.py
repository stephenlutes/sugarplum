import os


def _read_file(file_path: str) -> str:
    with open(os.environ["SUGARPLUM_BASE_PATH"] + "/" + file_path) as f:
        return f.read()


def get_input(year: int, day: int) -> str:
    return _read_file(f"{year}/{day:02}/data.in")
