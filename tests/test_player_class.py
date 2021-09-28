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


def test_player_2_pulls_up_to_seven(player_2, bag):
    player_2.tray = [LetterTile("A", 1), LetterTile("A", 1)]
    player_2.pull_tiles(bag)
    assert len(player_2.tray) == 7


def test_player_2_stops_pulling_when_bag_is_empty(player_2, bag):
    while len(bag.keys()) > 1:
        bag.pull_tile()
    player_2.tray = []
    player_2.pull_tiles(bag)
    assert len(player_2.tray) != 7


def test_player_1_sort_keys(player_1):
    player_1.tray = [LetterTile("A", 1), LetterTile("B", 3)]
    player_1.sort_tray()
    assert player_1.show_tray() == "A  B"


def test_player_1_sort_keys_reverse(player_1):
    player_1.tray = [LetterTile("A", 1), LetterTile("B", 3)]
    player_1.sort_tray(reverse=True)
    assert player_1.show_tray() == "B  A"
