 # CS 369 AI & Machine Learning
Fall 2025

**Instructor**: [Peter Drake](https://sites.google.com/a/lclark.edu/drake/home)  
**Teaching assistant**: [Ishan Abraham](mailto:ishanabraham@lclark.edu)  
**Meetings**: 12:40-1:50 PM MWF, Olin 305  
**Final presentations**: 8:30-11:30 AM, Tuesday, December 16

## Getting Help
* Write to the [course email list](mailto:25fa-cs-369-01@lclark.edu) 24/7
* Come to the TA's lab hours,                   .
* [Make an appointment to see me](https://calendar.app.google/qegvZRaPJ5mScdCz5) or drop by my office

## Course Text
Géron, [*Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems, 3rd Edition*](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/)  
There are [associated Jupyter notebooks](https://github.com/ageron/handson-ml3).
### Suggested Text
No readings will be assigned, but if you want another take on a topic or to read more deeply, this is also on reserve in the library:  
Chollet and Watson, [*Deep Learning with Python, Third Edition*](https://www.manning.com/books/deep-learning-with-python-third-edition)

## Links
[Course Policies](https://github.com/PeterDrake/drakepedia/blob/master/administrivia/policies.md)  
[Class Notes](https://github.com/PeterDrake/cs369/tree/main/lessons)  
[In-Class Code](https://github.com/PeterDrake/cs369_f25_in_class/)  
[Pythonorama](https://github.com/alainkaegi/pythonorama/blob/main/README.md)

## Collaborative Documents
[Ripped From Today's Headlines](https://docs.google.com/spreadsheets/d/14O6o5iE4JBWry8kl5O2hcp1EOm4DjLlLjagIs2C-CCw/edit?usp=sharing)  
[Social Context Books](https://docs.google.com/spreadsheets/d/1r3B2jbbaaml8tAtgwQx4qP-1F_PaLW5806LzUGphZVM/edit?usp=sharing)

## Overview
This course examines the philosophical, theoretical, and practical issues involved in the design of thinking machines. We will explore techniques used to get computers to solve problems that once were (and in some cases still are) thought to be strictly in the domain of human intelligence. The bulk of the course will focus on machine learning: building systems that can be trained from data rather than explicitly programmed.

The prerequisite for this course is CS 171 (Computer Science I) and either CS 172 (Computer Science II) or DSCI 140 (Introduction to Data Science). You are expected to be proficient with general programming concepts such as variables, if/else statements, loops, and functions.

We will use the Python programming language. If you haven't used it before, you *have* learned a couple of other languages (probably C and R), so you should be able to pick it up quickly. Take advantage of Pythonorama and the "Getting Help" options above to get up to speed. If you want a textbook on Python, good choices are Downey, [*Think Python: How To Think Like a Computer Scientist*](https://allendowney.github.io/ThinkPython/index.html) (free online) or Lubanovic, [*Introducing Python: Modern Computing in Simple Packages, 2nd Edition*](http://shop.oreilly.com/product/0636920252528.do).

## Learning Objectives
Upon completing this course, you should be able to:

* frame AI and machine learning tasks as search for a point, path, or policy in some mathematical space.
* discuss the role of AI and machine learning in present-day society, including issues of privacy, bias, and power structures.
* use, implement, explain, and compare classical search algorithms, including depth-first, breadth-first, iterative-deepening, A*, and hill-climbing / gradient descent.
* use, implement, explain, and compare adversarial search algorithms, including minimax and Monte Carlo tree search.
* use, implement, explain, and compare machine learning techniques, including k-means clustering, k-nearest neighbors, linear regression, logistic regression, decision trees, random forests, genetic algorithms, and neural networks (including deep convolutional neural networks).
* explain and address practical problems surrounding machine learning, such as data cleaning and overfitting.

## Course Structure
The major components of the course are:
* Individual assignments that you are meant to complete on your own. You are welcome to help each other with *concepts*, but any code, writing, math, etc. should be your own.
* Team projects that you complete with a team of 3-4 students.
* Reading and reporting on a book about the social context of AI and machine learning. To keep discussions interesting, and to spare me the tedium of reading dozens of essays on the same book, each student will read a different book.

There are no exams. In place of a final exam, each student will give a very short (5 minute) presentation on the book they read. This will be accompanied by a class discussion.

## Schedule
Flex days are days for you to work on assignments in class. They also serve as a reserve in case of getting behind,
instructor illness, inclement weather, etc. Note the links to class notes above.

| Day | Date   | Lesson                                                   |
|-----|--------|----------------------------------------------------------|
| Wed | Sep 3  | AI: Should We Be Doing This?                             |
| Fri | Sep 5  | Syllabus and Setup                                       |
| Mon | Sep 8  | Python Review                                            |
| Wed | Sep 10 | Agents                                                   |
| Fri | Sep 12 | Flex                                                     |
| Mon | Sep 15 | Uninformed Search                                        |
| Wed | Sep 17 | Heuristic Search                                         |
| Fri | Sep 19 | Adversarial Search                                       |
| Mon | Sep 22 | Adversarial Search Continued                             |
| Wed | Sep 24 | Monte Carlo Tree Search                                  |
| Fri | Sep 26 | Flex                                                     |
| Mon | Sep 29 | The Turing Test                                          |
| Wed | Oct 1  | Machine Learning                                         |
| Fri | Oct 3  | Linear Regression                                        |
| Mon | Oct 6  | Gradient Descent                                         |
| Wed | Oct 8  | Logistic Regression                                      |
| Mon | Oct 13 | Classification                                           |
| Wed | Oct 15 | Decision Trees                                           |
| Fri | Oct 17 | Ensemble Learning                                        |
| Mon | Oct 20 | Unsupervised Learning                                    |
| Wed | Oct 22 | Neural Networks                                          |
| Fri | Oct 24 | Backpropagation                                          |
| Mon | Oct 27 | Bias and Privacy                                         |
| Wed | Oct 29 | NumPy                                                    |
| Fri | Oct 31 | TensorFlow                                               |
| Mon | Nov 3  | Flex                                                     |
| Wed | Nov 5  | Using BLT                                                |
| Fri | Nov 7  | Flex                                                     |
| Mon | Nov 10 | Deep Learning                                            |
| Wed | Nov 12 | Convolution                                              |
| Fri | Nov 14 | Flex                                                     |
| Mon | Nov 17 | Flex                                                     |
| Wed | Nov 19 | Autoencoders                                             |
| Fri | Nov 21 | Flex                                                     |
| Mon | Nov 24 | Generative Adversarial Networks                          |
| Wed | Nov 26 | Transformers                                             |
| Mon | Dec 1  | Large Language Models and Retrieval Augmented Generation |
| Wed | Dec 3  | Reinforcement Learning                                   |
| Fri | Dec 5  | Flex                                                     |
| Mon | Dec 8  | Genetic Algorithms                                       |
| Wed | Dec 10 | Review                                                   |
| Tue | Dec 16 | Final presentations, 8:30-11:30 AM                       |

