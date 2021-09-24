from typing import *
import pytest
import sys

sys.path.append("..")
from scrabble.scrabble import Letter


@pytest.mark.xfail(raises=AttributeError)
def test_is_frozen():
    lt = Letter("A", 1, 9)
    lt.amount = 0
    print(lt.amount)


@pytest.mark.parametrize(
    "test_input, letter",
    [
        (("A", 1, 9), "a"),
        (("A", 1, 9), "A"),
        (("H", 4, 2), "H"),
        (("I", 1, 9), "i"),
        (("", 0, 2), "A"),
    ],
)
def test_letter_vs_str_pass(test_input: tuple, letter: str):
    assert Letter(*test_input) == letter


@pytest.mark.parametrize(
    "test_input, letter",
    [
        (("B", 3, 2), "a"),
        (("A", 1, 9), "B"),
    ],
)
def test_letter_vs_str_fail(test_input: tuple, letter: str):
    assert Letter(*test_input) != letter


@pytest.mark.parametrize(
    "test_input, test_letter",
    [
        (("", 0, 2), ("", 0, 2)),
        (("A", 1, 9), ("", 0, 2)),
        (("", 0, 2), ("A", 1, 9)),
        (("A", 1, 9), ("A", 1, 9)),
        (("H", 4, 2), ("H", 4, 2)),
    ],
)
def test_letter_vs_letter_pass(test_input: tuple, test_letter: tuple):
    assert Letter(*test_input) == Letter(*test_letter)


@pytest.mark.parametrize(
    "test_input, test_letter",
    [
        (("A", 1, 9), ("H", 4, 2)),
        (("A", 1, 9), ("I", 1, 9)),
    ],
)
def test_letter_vs_letter_fail(test_input: tuple, test_letter: tuple):
    assert Letter(*test_input) != Letter(*test_letter)


@pytest.mark.parametrize(
    "test_input, other",
    [
        (("A", 1, 9), ("H", 4, 2)),
        (("A", 1, 9), "('H', 4, 2)"),
        (("A", 1, 9), "Blah"),
    ],
)
def test_letter_vs_other(test_input: tuple, other: Any):
    assert Letter(*test_input) != other


@pytest.mark.parametrize(
    "letter, sub, expected",
    [
        (("", 0, 2), 1, 1),
        (("A", 1, 9), 4, 5),
        (("H", 4, 1), 1, 0),
    ],
)
def test_letter_subtract(letter: tuple, sub: int, expected: int):
    lt = Letter(*letter)
    _ = lt - sub
    assert lt.amount == expected


@pytest.mark.parametrize(
    "letter, sub, expected",
    [
        (("", 0, 2), 1.0, 1),
        (("A", 1, 9), "H", 5),
        (("H", 4, 1), 15, 0),
    ],
)
@pytest.mark.xfail(raises=ValueError)
def test_letter_subtract(letter: tuple, sub: int, expected: int):
    lt = Letter(*letter)
    _ = lt - sub
    assert lt.amount == expected
