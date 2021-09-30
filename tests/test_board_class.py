import pytest
from scrabble.board import Board


@pytest.fixture(scope='module')
def board():
    return Board()


def test_board_is_correct_height(board):
    assert len(board.current_board)


def test_board_is_correct_width(board):
    assert len(board.current_board[0])
