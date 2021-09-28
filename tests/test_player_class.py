import pytest
from scrabble.player import Player
from scrabble.bag import LetterBag, LetterTile


@pytest.fixture(scope="module")
def bag() -> LetterBag:
    return LetterBag()


@pytest.fixture(scope="module")
def player_1():
    return Player("Player 1")


@pytest.fixture(scope="module")
def player_2():
    return Player("Player 2")


def test_player_1_repr(player_1):
    assert repr(player_1) == "Player(user=Player 1)"


def test_player_1_pulls_seven_tiles(player_1, bag):
    player_1.pull_tiles(bag)
    assert len(player_1.tray) == 7
