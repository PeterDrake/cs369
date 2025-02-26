# Overview
This assignment asks you to complete an algorithm for building a decision tree from data on choosing a restaurant. (The data come from *Russell and Norvig, Artificial Intelligence: A Modern Approach, Fourth Edition*.) In addition to a deeper understanding of this algorithm, you will also gain more experience with object-oriented programming in Python.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Files
[`decision_tree.py`](../src/decision_tree.py)  
[`test_decision_tree.py`](../test/test_decision_tree.py)

You will be completing some methods in `decision_tree.py`.

# Algorithm
You'll be using the CART algorithm, as described at the beginning of chapter 6 of Géron. Since your attributes are discrete rather than continuous, rather than setting a threshold, your internal (non-leaf) tree nodes will distinguish one value from another. For example, one node might ask if the 'Price' attribute has the value '$$' or not.

# Printing the Tree
By defining the `__str__` "magic" method, you will allow your Tree to be printed. It should be printed in outline form, with the children of each node indented below it.

Here are the first four lines of the output of my solution:

```
Patrons == Some?
  True
  Hungry == False?
	False
```

# Optional Challenge Problems
* Modify the tree to allow for nonbinary decisions. For example, one node might split on the 'Price' attribute and have three children, one for each possible value of that attribute.
* Allow the option to limit the depth of the tree (by passing an extra argument to the initializer).

# What to Hand in
Hand in your completed version of `decision_tree.py`, which passes all the tests in `test_decision_tree.py`.
