# Overview
This assignment asks your pair to complete an artificially intelligent player for the game of [*Othello*](https://en.wikipedia.org/wiki/Reversi) (also known as *Reversi*).

**This is a pair assignment. When you are done, one member of your pair should submit the file, including (as a comment at the top of the file) the names of everyone who contributed. If you are unfamiliar with pair programming watch [this short video](https://www.youtube.com/watch?v=rG_U12uqRhE).**

# Files
* [test_othello.py](../test/test_othello.py)
* [othello.py](../src/othello.py)

Your job is to complete the functions in `othello.py` so that all of the tests pass. You can then run `othello.py` to play against the computer! You can increase the search depth in the call to `best_move` in `main` to make the program smarter but slower.

# Hints
If you are unfamiliar with Othello, you can [play an existing version online](https://www.eothello.com/).

In this game, the moves available depend on the current player.

If a player can’t capture anything, they are required to pass. The game ends when neither player has a move.

The code we developed for *Tic-Tac-Toe* will be extremely helpful.

Look at the documentation for the various functions.

In this game, `winner` has been replaced with `score`. This both gives the score at the end of the game and serves as a static evaluation function when the game is not over.

Since (unlike in *Tic-Tac-Toe*) the program does not search all the way to the end of the game, there is an extra argument for the depth of the search in `value` and `best_move`. A depth of 0 means to make no recursive calls.

# Optional Challenge Problems
Modify main to watch the program play against itself. Can you make one player search to depth 5 while the other only searches to depth 1?

Develop a graphic user interface for the game using a library such as `tkinter` or `pygame`.

Learn about and implement [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning). Find some measurement, like time or number of nodes explored, to demonstrate that this version finds the same answer faster. This improvement might allow you to search more deeply in a given amount of time.

# What to Hand in
One member of your pair should hand in your completed version of `othello.py`. Be sure to fill in the names of everyone who contributed in the comment at the top.

*Both* of you should also fill in the [peer feedback form](https://docs.google.com/forms/d/e/1FAIpQLSe83mXCj-epu2kQ6LGW57OdCpSK5oZLgQHd7J5Nnx5MxYSsFQ/viewform?usp=sharing). If you are in a three-person team, fill it out once for each of your partners.
