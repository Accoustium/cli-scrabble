import copy
import random
from typing import *
from .letter import LetterTile


class LetterBag(dict):
    def __init__(self):
        super().__init__()

        self.update(
            {
                LetterTile("A", 1): 9,
                LetterTile("B", 3): 2,
                LetterTile("C", 3): 2,
                LetterTile("D", 2): 4,
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
                LetterTile("", 0): 2,
            }
        )

    def __getitem__(self, item: Union[LetterTile, str]):
        _item = copy.copy(item)

        if isinstance(item, str):
            if item in self.keys():
                item = self._find_key(item)

        if isinstance(item, LetterTile):
            return super().__getitem__(item)

        raise KeyError(_item)

    def keys(self) -> List:
        return [str(x) for x in self]

    def _find_key(self, other: Union[LetterTile, str]):
        if isinstance(other, LetterTile) or isinstance(other, str):
            for key in self:
                if key == other:
                    return key

        raise KeyError(other)

    def pull_tile(self):
        if self == {}:
            return None
        keys = self.keys()
        random_int = int(random.random() * len(keys))
        tile = self._find_key(keys[random_int])
        if self[tile] > 1:
            self[tile] -= 1
            return tile
        else:
            self.pop(tile)
            return tile
