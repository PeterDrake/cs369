# Overview

This assignment asks you to apply uninformed search to the classic *N Queens* problem: arranging $n$ queens on an $n \times n$ *Chess* board so that no two are in the same row, column, or diagonal.

Specifically, you will write a function `nqueens` that takes a number `n` and returns a list or tuple of `n` row numbers for the queens. Each number 0 through `n` - 1 should appear exactly once. For example, `nqueens(8)` might return:

`(6, 4, 2, 0, 5, 7, 1, 3)`

which corresponds to this solution (with the rows numbered from the top):

![Chess board with one queen in each colum, in rows 6, 4, 2, 0, 5, 7, 1, and 3](https://upload.wikimedia.org/wikipedia/commons/9/93/%D7%97%D7%99%D7%93%D7%AA_%D7%A9%D7%9E%D7%95%D7%A0%D7%94_%D7%94%D7%9E%D7%9C%D7%9B%D7%95%D7%AA.jpg)

The queen in the first column is in row 6, the next one is in row 4, and so on.

If there is no solution, your function should return `False`.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Representation
How you represent the problem and the available actions has a huge effect on the difficulty of this problem. Consider the following options:

* Start with all of the queens on the bottom row. On each step, move one queen.
* Start with an empty board. On each step, add one queen so that it does not attack any of the others.
* Start with an empty board. On the first step, add one queen to the first column. On each step, add one queen to the next column so that it does not attack any of the previous queens.

The first option does not guarantee that a solution will be found (or the lack of a solution proven) in $n$ moves. The second option has a much higher branching factor than the third. We therefore choose the third option.

# Algorithm
Use depth-limited search, implemented recursively (rather than with an explicit data structure for the frontier). In loose pseudocode, start with an empty list and then:

1. If you've already placed all `n` queens, return the solution
2. Otherwise, for each row in the next column:
   * If you can solve the puzzle by placing the next queen in that row and then recurring, return that solution
3. If no solution was found, return `False`

Note that, when you add a queen, you should create a *new* list or tuple rather than modifying the existing one. The optional challenge problem below discusses an alternative.

# Testing
You can generate solutions for small values of `n` and verify them by hand. A unit test file is also provided.

Note that there is no solution if `n` is 2 or 3.

# Files
[test_nqueens.py](../test/test_nqueens.py)

# Optional Challenge Problem: Backtracking Search
Write an additional function `nqueens_backtracking` that implements backtracking search. This is almost identical to depth-first search, except that when you add a queen, you modify your existing solution rather than creating a copy. This means that, if that queen doesn't lead to a solution, you have to remove it before adding one in a different column.

This uses less memory and avoids the overhead of making copies. Does it run faster in practice than the standard version for large values of `n`? I don't know -- I haven't tried it yet!

# What to Hand in
Hand in a single file `nqueens.py` containing your function `nqueens` and any other functions you need.
