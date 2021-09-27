from typing import *
from collections import namedtuple


class LetterTile(namedtuple("LETTER", "char value")):
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
