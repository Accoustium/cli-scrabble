from typing import *
from collections import namedtuple
import sys

sys.path.append("..")
from scrabble.bag import LetterTile
from scrabble.player import Player


class Point(namedtuple("POINT", "x y")):
    pass


class Board:
    size: tuple = (15, 15)
    triple_word: tuple = (
        Point(0, 0), Point(7, 0), Point(14, 0),
        Point(0, 7), Point(14, 7),
        Point(0, 14), Point(7, 14), Point(14, 14),
    )
    double_word: tuple = (
        Point(1, 1), Point(13, 1),
        Point(2, 2), Point(12, 2),
        Point(3, 3), Point(11, 3),
        Point(4, 4), Point(10, 4),
        Point(7, 7),
        Point(4, 10), Point(10, 10),
        Point(3, 11), Point(11, 11),
        Point(2, 12), Point(12, 12),
        Point(1, 13), Point(13, 13),
    )
    triple_letter: tuple = (
        Point(5, 1), Point(9, 1),
        Point(1, 5), Point(5, 5), Point(9, 5), Point(13, 5),
        Point(1, 9), Point(5, 9), Point(9, 9), Point(13, 9),
        Point(5, 13), Point(9, 13),
    )
    double_letter: tuple = (
        Point(3, 0), Point(11, 0),
        Point(6, 2), Point(8, 2),
        Point(0, 3), Point(7, 3), Point(15, 3),
        Point(2, 6), Point(6, 6), Point(8, 6), Point(12, 6),
        Point(3, 7), Point(11, 7),
        Point(2, 8), Point(6, 8), Point(8, 8), Point(12, 8),
        Point(0, 11), Point(7, 11), Point(15, 11),
        Point(6, 12), Point(8, 12),
        Point(3, 14), Point(11, 14),
    )

    def __init__(self):
        self.current_board: List[List[Union[None, LetterTile]]] = [[None] * self.size[0]] * self.size[1]

    def play_word(self, word_entry: str, player: Player, starting_point: Point):
        pass
