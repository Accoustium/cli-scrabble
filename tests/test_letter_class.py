from typing import *
import pytest
import sys

sys.path.append("..")
from scrabble.scrabble import LetterTile


@pytest.mark.parametrize(
    "test_input, letter",
    [
        (("A", 1), "a"),
        (("A", 1), "A"),
        (("H", 4), "H"),
        (("I", 1), "i"),
        (("", 0), "A"),
    ],
)
def test_letter_vs_str_pass(test_input: tuple, letter: str):
    assert LetterTile(*test_input) == letter


@pytest.mark.parametrize(
    "test_input, letter",
    [
        (("B", 3), "a"),
        (("A", 1), "B"),
    ],
)
def test_letter_vs_str_fail(test_input: tuple, letter: str):
    assert LetterTile(*test_input) != letter


@pytest.mark.parametrize(
    "test_input, test_letter",
    [
        (("", 0), ("", 0)),
        (("A", 1), ("", 0)),
        (("", 0), ("A", 1)),
        (("A", 1), ("A", 1)),
        (("H", 4), ("H", 4)),
    ],
)
def test_letter_vs_letter_pass(test_input: tuple, test_letter: tuple):
    assert LetterTile(*test_input) == LetterTile(*test_letter)


@pytest.mark.parametrize(
    "test_input, test_letter",
    [
        (("A", 1), ("H", 4)),
        (("A", 1), ("I", 1)),
    ],
)
def test_letter_vs_letter_fail(test_input: tuple, test_letter: tuple):
    assert LetterTile(*test_input) != LetterTile(*test_letter)


@pytest.mark.parametrize(
    "test_input, other",
    [
        (("A", 1), ("H", 4)),
        (("A", 1), "('H', 4, 2)"),
        (("A", 1), "Blah"),
    ],
)
def test_letter_vs_other(test_input: tuple, other: Any):
    assert LetterTile(*test_input) != other
