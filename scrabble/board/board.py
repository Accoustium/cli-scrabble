from typing import *
import sys

sys.path.append('..')
from scrabble.bag import LetterTile


class Board:
    size: tuple = (15, 15)
    triple_word: tuple = (
        (0, 0), (7, 0), (14, 0),
        (0, 7), (14, 7),
        (0, 14), (7, 14), (14, 14),
    )
    double_word: tuple = (
        (1, 1), (13, 1),
        (2, 2), (12, 2),
        (3, 3), (11, 3),
        (4, 4), (10, 4),
        (7, 7),
        (4, 10), (10, 10),
        (3, 11), (11, 11),
        (2, 12), (12, 12),
        (1, 13), (13, 13),
    )
    triple_letter: tuple = (
        (5, 1), (9, 1),
        (1, 5), (5, 5), (9, 5), (13, 5),
        (1, 9), (5, 9), (9, 9), (13, 9),
        (5, 13), (9, 13),
    )
    double_letter: tuple = (
        (3, 0), (11, 0),
        (6, 2), (8, 2),
        (0, 3), (7, 3), (15, 3),
        (2, 6), (6, 6), (8, 6), (12, 6),
        (3, 7), (11, 7),
        (2, 8), (6, 8), (8, 8), (12, 8),
        (0, 11), (7, 11), (15, 11),
        (6, 12), (8, 12),
        (3, 14), (11, 14),
    )

    def __init__(self):
        self.current_board: List[List[Union[None, LetterTile]]] = [[None] * self.size[0]] * self.size[1]
