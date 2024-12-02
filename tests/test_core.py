from pathlib import Path

import pytest

from sugarplum import get_input

YEAR: int = 2023
DAY: int = 24


@pytest.fixture(autouse=True)
def base_path(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setenv("SUGARPLUM_BASE_PATH", str(tmp_path))


@pytest.fixture(autouse=True)
def setup_dirs(tmp_path: Path) -> None:
    (tmp_path / str(YEAR)).mkdir()
    (tmp_path / f"{YEAR}/{DAY}").mkdir()


def create_file(path: Path, data: str) -> None:
    with open(path, "w") as f:
        f.write(data)


def test_puzzle_input_data_is_read(tmp_path: Path) -> None:
    expected: str = "North Pole"
    create_file(tmp_path / f"{YEAR}/{DAY}/data.in", expected)

    assert get_input(YEAR, DAY) == expected


def test_day_number_gets_zero_padded(tmp_path: Path) -> None:
    expected: str = "sleigh"
    day: int = 3
    dir_path: Path = tmp_path / f"{YEAR}/{day:02}"
    dir_path.mkdir()
    create_file(dir_path / "data.in", expected)

    assert get_input(YEAR, day) == expected
