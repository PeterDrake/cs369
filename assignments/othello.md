# Overview
This assignment asks your team to complete an artificially intelligent player for the game of [*Othello*](https://en.wikipedia.org/wiki/Reversi) (also known as *Reversi*).

**This is a team assignment. When you are done, *one* member of your team should submit the file, including (as a comment at the top of the file) the names of everyone who contributed.**

# Files
* [`othello.py`](../src/othello.py)
* [`test_othello.py`](../test/test_othello.py)

Your job is to complete the functions in `othello.py` so that all of the tests pass. You can then run `othello.py` to play against the computer! You can increase the search depth in the call to `best_move` in `main` to make the program smarter but slower.

# On Working as a Team
This project is, intentionally, too much for one student to complete in a reasonable amount of time. You will need to work together as a team!

The first thing to work out is communication and scheduling. Exchange email addresses or phone numbers. Set up a group chat or other means of communication. Figure out when you can meet to work on the project. It will take several hours. It's best if you can all work together, but if not, figure out who can work at what times and plan to hand off the code to the rest of the team after each session.

When working, it's a good idea to use [pair programming](https://www.youtube.com/watch?v=rG_U12uqRhE).

Break the problem down into steps. Have one pair (or person) do the first step, then a different pair do the next step, and so on. Here's a good sequence for this assignment:

1. Have everyone play the game, so you understand the rules.
1. Make sure everyone has the code and can run the tests.
1. Pass `test_finds_successor`.
1. Pass `test_finds_score`.
1. Pass `test_finds_value_1`.
1. Pass `test_finds_value_2`.
1. Pass `test_finds_best_move_shallow`.
1. Pass `test_finds_best_move_medium`.
1. Pass `test_finds_best_move_deep`.
1. Clean up the code: remove commented-out code, improve names of local variables, eliminate redundancy, etc.
1. If you have time, save a copy and then consider tackling optional challenge problems.
1. Clean up the code again.
1. Have *one person* hand in your solution with everyone's names on it.

Remember to trade off who is "driving" (typing) after each step. Avoid having someone who never gets a chance to contribute or someone who "heroically" does almost all of the work. If you feel your teammates are more experienced than you, ask questions! If you feel you are more experienced, be patient and remember that making your team stronger is more important than completing the project as quickly as possible.

# Hints
If you are unfamiliar with Othello, you can [play an existing version online](https://www.eothello.com/).

In this game, the moves available depend on the current player.

If a player can’t capture anything, they are required to pass. The game ends when neither player has a move.

The code we developed for *Tic-Tac-Toe* will be extremely helpful.

Look at the documentation for the various functions.

In this game, `winner` has been replaced with `score`. This both gives the score at the end of the game and serves as a static evaluation function when the game is not over.

Since (unlike in *Tic-Tac-Toe*) the program does not search all the way to the end of the game, there is an extra argument for the depth of the search in `value` and `best_move`. A depth of 0 means to make no recursive calls.

# Optional Challenge Problems
Modify `main` to watch the program play against itself. Can you make one player search to depth 5 while the other only searches to depth 1?

Develop a graphic user interface for the game using a library such as `tkinter` or `pygame`.

Learn about and implement [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning). Find some measurement, like time or number of nodes explored, to demonstrate that this version finds the same answer faster. This improvement might allow you to search more deeply in a given amount of time.

# What to Hand in
*One* member of your team should hand in your completed version of `othello.py`. Be sure to fill in the names of everyone who contributed in the comment at the top.
