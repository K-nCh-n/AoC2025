from pathlib import Path
from typing import List, Tuple, Iterable


def read_input(day: int) -> List[str]:
    """
    Reads the input file for a given day from ../input/dayXX.txt.
    Returns a list of lines.
    """
    input_path = Path(__file__).parent.parent / "input" / f"day{day:02}.txt"
    return input_path.read_text().splitlines()

def read_ints(day: int) -> List[int]:
    """
    Reads lines of integers.
    Example:
        5
        12
        37
    """
    return [int(x) for x in read_input(day)]


def ints(s: str) -> List[int]:
    """Extracts all integers from a string. Example: "5 12 37" -> [5, 12, 37]"""
    import re
    return list(map(int, re.findall(r"-?\d+", s)))


def chunks(lst: List, size: int) -> Iterable[List]:
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), size):
        yield lst[i:i+size]


def neighbors4(r: int, c: int) -> Iterable[Tuple[int, int]]:
    """Up, Down, Left, Right."""
    return [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]


def neighbors8(r: int, c: int) -> Iterable[Tuple[int, int]]:
    """8-direction grid neighbors."""
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == 0 and dc == 0:
                continue
            yield (r + dr, c + dc)

