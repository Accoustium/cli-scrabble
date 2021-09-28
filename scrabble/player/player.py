import sys

sys.path.append("../..")
from scrabble.bag import LetterBag


class Player:
    def __init__(self, username: str, firstname: str = None, lastname: str = None):
        self.first_name = firstname
        self.last_name = lastname
        self.username = username
        self.tray = []

    def __repr__(self):
        return f"Player(user={self.username})"

    def pull_tiles(self, bag: LetterBag):
        while len(self.tray) >= 7:
            tile = bag.pull_tile()
            if tile is None:
                break

            self.tray.append(tile)

    def show_tray(self):
        return ["  ".join(map(str, self.tray))]

    def sort_tray(self, reverse=False):
        self.tray.sort(key=lambda x: x.char, reverse=reverse)
