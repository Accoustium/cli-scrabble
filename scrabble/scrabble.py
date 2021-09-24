from typing import *


class Letter:
    def __init__(self, char: str, score: int, amount: int):
        self.__dict__["char"]: str = char
        self.__dict__["score"]: int = score
        self.__dict__["amount"]: int = amount

    def __setattr__(self, key, value):
        raise AttributeError("can't set attribute")

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

    def __sub__(self, other):
        if isinstance(other, int):
            if other <= self.amount:
                self.__dict__["amount"] -= other
                return

        raise ValueError

    def _is_blank(self):
        return self.char == ""
