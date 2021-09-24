from typing import *
import collections


LETTER = collections.namedtuple('LETTER', ['char', 'score', 'amount'])


class Letter(LETTER):
    char: str
    score: int
    amount: int

    def __eq__(self, other: Union[object, str]):
        if not isinstance(other, Letter):
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
        return self.char == ''
