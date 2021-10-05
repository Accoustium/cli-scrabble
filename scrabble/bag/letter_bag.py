import copy
import random
from typing import *
from .letter import LetterTile, Alphabet


ALPHABET = Alphabet()


class LetterBag(dict):
    def __init__(self):
        super().__init__()

        self.update(
            {
                ALPHABET.A: 9,
                ALPHABET.B: 2,
                ALPHABET.C: 2,
                ALPHABET.D: 4,
                ALPHABET.E: 12,
                ALPHABET.F: 2,
                ALPHABET.G: 3,
                ALPHABET.H: 2,
                ALPHABET.I: 9,
                ALPHABET.J: 1,
                ALPHABET.K: 1,
                ALPHABET.L: 4,
                ALPHABET.M: 2,
                ALPHABET.N: 6,
                ALPHABET.O: 8,
                ALPHABET.P: 2,
                ALPHABET.Q: 1,
                ALPHABET.R: 6,
                ALPHABET.S: 4,
                ALPHABET.T: 6,
                ALPHABET.U: 4,
                ALPHABET.V: 2,
                ALPHABET.W: 2,
                ALPHABET.X: 1,
                ALPHABET.Y: 2,
                ALPHABET.Z: 1,
                ALPHABET.BLANK: 2,
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
