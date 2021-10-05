from typing import *
from collections import namedtuple


class LetterTile(namedtuple("LETTER", "char value")):
    def __hash__(self):
        return hash(repr(self))

    def __str__(self):
        if self._is_blank():
            return "[]"

        return self.char

    def __eq__(self, other: Union[object, str]):
        if not isinstance(other, LetterTile):
            if not isinstance(other, str):
                return False
            else:
                if self._is_blank():
                    return True

                return self.char == other.upper()
        else:
            if self._is_blank() or other._is_blank():
                return True

            return self.char == other.char

    def _is_blank(self):
        return self.char == ""


class Alphabet:
    letter_scores: tuple = (
        ("A", 1), ("B", 3), ("C", 3), ("D", 2),
        ("E", 1), ("F", 4), ("G", 2), ("H", 4),
        ("I", 1), ("J", 8), ("K", 5), ("L", 1),
        ("M", 3), ("N", 1), ("O", 1), ("P", 3),
        ("Q", 10), ("R", 1), ("S", 1), ("T", 1),
        ("U", 1), ("V", 4), ("W", 4), ("X", 8),
        ("Y", 1), ("Z", 10), ("", 0)
    )

    def __init__(self):
        self._build_alphabet()

    def _build_alphabet(self):
        for letter, score in self.letter_scores:
            _letter = letter if letter != "" else 'BLANK'
            eval('self.__dict__.update({' + f'"{_letter}": LetterTile("{letter}", {score})' + '})')
