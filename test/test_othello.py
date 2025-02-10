from othello import *

def test_finds_flips():
    board = ('........',
             '........',
             '...OX...',
             '..XXXX..',
             '..XXXOXX',
             '...O.XO.',
             '........',
             '........')
    result = flips(board, 'O', (4, 1))
    assert set(result) == {(3, 2), (4, 2), (4, 3), (4, 4)}

def test_finds_successor():
    board = ('........',
             '........',
             '...OX...',
             '..XXXX..',
             '..XXXOXX',
             '...O.XO.',
             '........',
             '........')
    correct = ('........',
               '........',
               '...OX...',
               '..OXXX..',
               '.OOOOOXX',
               '...O.XO.',
               '........',
               '........')
    result = successor(board, 'O', (4, 1))
    assert result == correct

def test_finds_legal_moves():
    board = ('........',
             '........',
             '...OX...',
             '..XXXX..',
             '..XXXOXX',
             '...O.XO.',
             '........',
             '........')
    result = legal_moves(board, 'O')
    assert set(result) == {(2, 5), (2, 6), (3, 1), (3, 6), (4, 1), (5, 4), (6, 5)}

def test_finds_pass():
    board = ('........',
             '........',
             '........',
             '...XOX..',
             '........',
             '........',
             '........',
             '........')
    result = legal_moves(board, 'X')
    assert set(result) == {'pass'}

def test_finds_no_legal_moves_before_board_full():
    board = ('OOOOOOOO',
             'OOOOOOOO',
             'OOOOOOOO',
             'OOOOOOO.',
             'OOOOOO..',
             'OOOOOO.X',
             'OOOOOOO.',
             'OOOOOOOO')
    assert set(legal_moves(board, 'X')) == set()
    assert set(legal_moves(board, 'O')) == set()

def test_finds_score():
    board = ('XXXXXXXX',
             'XXXXXXXX',
             'XXXXXXXX',
             'XXXXXXXX',
             'OOOOOOOX',
             'OOOOOOOO',
             'OOOOOOOO',
             'OOOOOOOO')
    assert score(board) == 2

def test_finds_value_1():
    board = ('........',
             '........',
             '...OX...',
             '..XXXX..',
             '..XXXOXX',
             '...O.XO.',
             '........',
             '........')
    assert value(board, 'O', 1) == -2

def test_finds_value_2():
    board = ('........',
             '........',
             '...OX...',
             '..XXXX..',
             '..XXXOXX',
             '...O.XO.',
             '........',
             '........')
    assert value(board, 'O', 2) == 7

def test_finds_best_move_shallow():
    board = ('XXXXXXXX',
             'XXXXXXXX',
             'XXXXXXXX',
             '..OXXXXO',
             'OOOOOOOO',
             'OOOOOOOO',
             'OOOOOOOO',
             'XOOOOOOO')
    assert best_move(board, 'X', 1) == (3, 0)

def test_finds_best_move_medium():
    board = ('........',
             'OXOXX...',
             '........',
             '........',
             '........',
             '........',
             '........',
             'OX......')
    assert best_move(board, 'O', 2) == (7, 2)

def test_finds_best_move_deep():
    board = ('........',
             'OXOXX...',
             '........',
             '........',
             '........',
             '........',
             '........',
             'OX......')
    assert best_move(board, 'O', 3) == (1, 5)
