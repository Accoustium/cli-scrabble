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
    letters = [
        LetterTile("A", 1),
        LetterTile("B", 3),
        LetterTile("C", 3),
        LetterTile("D", 2),
        LetterTile("E", 1),
        LetterTile("F", 4),
        LetterTile("G", 2),
        LetterTile("H", 4),
        LetterTile("I", 1),
        LetterTile("J", 8),
        LetterTile("K", 5),
        LetterTile("L", 1),
        LetterTile("M", 3),
        LetterTile("N", 1),
        LetterTile("O", 1),
        LetterTile("P", 3),
        LetterTile("Q", 10),
        LetterTile("R", 1),
        LetterTile("S", 1),
        LetterTile("T", 1),
        LetterTile("U", 1),
        LetterTile("V", 4),
        LetterTile("W", 4),
        LetterTile("X", 8),
        LetterTile("Y", 1),
        LetterTile("Z", 10),
        LetterTile("", 0),
    ]
    for letter in letters:
        amount = bag.pop(letter, None)
    bag.update(
        {
            LetterTile("A", 1): 2,
            LetterTile("L", 1): 1,
            LetterTile("T", 1): 2,
        }
    )
    player_2.tray = []
    player_2.pull_tiles(bag)
    assert len(player_2.tray) != 7


def test_player_1_sort_tray(player_1):
    player_1.tray = [LetterTile("A", 1), LetterTile("B", 3)]
    player_1.sort_tray()
    assert player_1.show_tray() == "A  B"


def test_player_1_sort_tray_multiple_letter(player_1):
    player_1.tray = [LetterTile("A", 1), LetterTile("B", 3), LetterTile("A", 1), LetterTile("A", 1)]
    player_1.sort_tray()
    assert player_1.show_tray() == "A  A  A  B"


def test_player_1_sort_tray_reverse(player_1):
    player_1.tray = [LetterTile("A", 1), LetterTile("B", 3)]
    player_1.sort_tray(reverse=True)
    assert player_1.show_tray() == "B  A"


def test_player_playing_tile_with_letter_tile_passing(player_2):
    player_2.tray = [LetterTile("A", 1), LetterTile("Z", 10)]
    assert player_2.play_tile(LetterTile("Z", 10))


def test_player_playing_tile_with_letter_tile_failing(player_2):
    player_2.tray = [LetterTile("A", 1), LetterTile("Z", 10)]
    assert not player_2.play_tile(LetterTile("B", 3))


def test_player_playing_tile_with_str_passing(player_2):
    player_2.tray = [LetterTile("A", 1), LetterTile("Z", 10)]
    assert player_2.play_tile("Z")


def test_player_playing_tile_with_lower_str_passing(player_2):
    player_2.tray = [LetterTile("A", 1), LetterTile("Z", 10)]
    assert player_2.play_tile("z")


def test_player_playing_tile_with_str_failing(player_2):
    player_2.tray = [LetterTile("A", 1), LetterTile("Z", 10)]
    assert not player_2.play_tile("B")
