from typing import *
import pytest
from scrabble.bag import *


@pytest.fixture(scope="module")
def bag():
    return LetterBag()


def test_bag_startup(bag: LetterBag):
    assert bag == {
        LetterTile("", 0): 2,
        LetterTile("A", 1): 9,
        LetterTile("B", 3): 2,
        LetterTile("C", 3): 2,
        LetterTile("D", 2): 3,
        LetterTile("E", 1): 12,
        LetterTile("F", 4): 2,
        LetterTile("G", 2): 3,
        LetterTile("H", 4): 2,
        LetterTile("I", 1): 9,
        LetterTile("J", 8): 1,
        LetterTile("K", 5): 1,
        LetterTile("L", 1): 4,
        LetterTile("M", 3): 2,
        LetterTile("N", 1): 6,
        LetterTile("O", 1): 8,
        LetterTile("P", 3): 2,
        LetterTile("Q", 10): 1,
        LetterTile("R", 1): 6,
        LetterTile("S", 1): 4,
        LetterTile("T", 1): 6,
        LetterTile("U", 1): 4,
        LetterTile("V", 4): 2,
        LetterTile("W", 4): 2,
        LetterTile("X", 8): 1,
        LetterTile("Y", 1): 2,
        LetterTile("Z", 10): 1,
    }


def test_find_amount_in_bag_by_letter(bag: LetterBag):
    assert bag["A"] == 9


def test_find_amount_in_bag_by_letter_class(bag: LetterBag):
    assert bag[LetterTile("A", 1)] == 9


def test_tile_pull(bag: LetterBag):
    tile = bag.pull_tile()
    assert isinstance(tile, LetterTile)


def test_tile_pull_stops_after_last_tile(bag: LetterBag):
    tile = bag.pull_tile()
    while tile is not None:
        tile = bag.pull_tile()

    assert bag == {}


@pytest.mark.xfail(raises=KeyError)
def test_key_error(bag: LetterBag):
    amount = bag["Zebra"]
