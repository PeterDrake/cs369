# CS 369 AI & Machine Learning
Spring 2025

**Instructor**: [Peter Drake](https://sites.google.com/a/lclark.edu/drake/home)  
**Teaching assistant**: [Katie Caudill](kcaudill@lclark.edu)  
**Meetings**: 1:50-2:50 PM MWF, Olin 305  
**Final presentations**: 1-4 PM, Monday, May 5

## Getting Help
* Write to the [course email list](25sp-cs-369-01@lclark.edu) 24/7
* Come to the TA's lab hours, 11 AM - 1 PM, Tuesdays, SQRC (JRHH 134)
* [Make an appointment to see me](https://calendar.app.google/XiynwHJNprXgGxWd8) or drop by my office

## Course Text
Géron, [*Hands-On Machine Learning with Scikit-Learn, Keras and TensorFlow: Concepts, Tools, and Techniques to Build Intelligent Systems, 3rd Edition*](https://www.oreilly.com/library/view/hands-on-machine-learning/9781098125967/)  
There are [associated Jupyter notebooks](https://github.com/ageron/handson-ml3).

## Links
[Course Policies](https://github.com/PeterDrake/drakepedia/blob/master/administrivia/policies.md)  
[Class Notes](https://github.com/PeterDrake/cs369/tree/main/lessons)  
[In-Class Code](https://github.com/PeterDrake/cs369_c25_in_class)
[Pythonorama](https://github.com/alainkaegi/pythonorama/blob/main/README.md)

## Collaborative Documents
[Glossary](https://docs.google.com/document/d/1_yoVjrNlc-iZGAU2MAyLnwFjJ8owK9oDaX6iDiwrOlA/edit?usp=sharing)  
[Dank Meme Stash](https://docs.google.com/document/d/1CbPZrWiyDVGtKfFFkldcgau_IJUd-OSWiIFsNM0GrQA/edit?usp=sharing)  
[AI Did Me Dirty](https://docs.google.com/document/d/1XL65wWGd1h24sOlXcnm6QfR3GhmxIljiUFFUIWV5GZU/edit?usp=sharing)  
[Ripped From Today's Headlines](https://docs.google.com/spreadsheets/d/1k9USK0J5Kcz1fqRcW5kFZiv7lE7XTp8P-JcOX_OpZfc/edit?usp=sharing)  
[Social Context Books](https://docs.google.com/spreadsheets/d/1iMZoGUTiqXl6eZQgCfdbSgisPi7yglwEa_SGP3H9e9Q/edit?usp=sharing)

## Overview
This course examines the philosophical, theoretical, and practical issues involved in the design of thinking machines. We will explore techniques used to get computers to solve problems that once were (and in some cases still are) thought to be strictly in the domain of human intelligence. The bulk of the course will focus on machine learning: building systems that can be trained from data rather than explicitly programmed.

The prerequisite for this course is CS 171 (Computer Science I) and either CS 172 (Computer Science II) or DSCI 140 (Introduction to Data Science). You are expected to be proficient with general programming concepts such as variables, if/else statements, loops, and functions.

We will use the Python programming language. If you haven't used it before, you *have* learned a couple of other languages (probably C and R), so you should be able to pick it up quickly. Take advantage of Pythonorama and the "Getting Help" options above to get up to speed. If you want a textbook on Python, a good choices are Downey, [*Think Python: How To Think Like a Computer Scientist*](https://allendowney.github.io/ThinkPython/index.html) (free online) or Lubanovic, [*Introducing Python: Modern Computing in Simple Packages, 2nd Edition*](http://shop.oreilly.com/product/0636920252528.do).

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
* Pair programming projects that you complete with another student. I will assign you a different partner for each such project.
* Reading and reporting on a book about the social context of AI and machine learning. To keep discussions interesting, and to spare me the tedium of reading dozens of essays on the same book, each student will read a different book.

There are no exams. In place of a final exam, each student will give a very short (5 minute) presentation on the book they read. This will be accompanied by a class discussion.

## Schedule
Flex days are days for you to work on assignments in class. They also serve as a reserve in case of getting behind,
instructor illness, inclement weather, etc. Note the links to class notes above.

| Day | Date   | Lesson                                                   |
|-----|--------|----------------------------------------------------------|
| Wed | Jan 22 | AI: Should We Be Doing This?                             |
| Fri | Jan 24 | Syllabus and Setup                                       |
| Mon | Jan 27 | Python Review                                            |
| Wed | Jan 29 | Agents                                                   |
| Fri | Jan 31 | Flex                                                     |
| Mon | Feb 3  | Uninformed Search                                        |
| Wed | Feb 5  | Heuristic Search                                         |
| Fri | Feb 7  | Adversarial Search                                       |
| Mon | Feb 10 | Adversarial Search Continued                             |
| Wed | Feb 12 | Monte Carlo Tree Search                                  |
| Fri | Feb 14 | The Turing Test                                          |
| Mon | Feb 17 | Machine Learning                                         |
| Wed | Feb 19 | Linear Regression                                        |
| Fri | Feb 21 | Gradient Descent                                         |
| Mon | Feb 24 | Logistic Regression                                      |
| Wed | Feb 26 | Measuring Learning                                       |
| Fri | Feb 28 | Decision Trees                                           |
| Mon | Mar 3  | Ensemble Learning                                        |
| Wed | Mar 5  | Unsupervised Learning                                    |
| Fri | Mar 7  | Neural Networks                                          |
| Mon | Mar 10 | Backpropagation                                          |
| Wed | Mar 12 | Flex                                                     |
| Fri | Mar 14 | Bias and Privacy                                         |
| Mon | Mar 17 | Using BLT                                                |
| Wed | Mar 19 | NumPy                                                    |
| Fri | Mar 21 | Flex                                                     |
| Mon | Mar 31 | TensorFlow                                               |
| Wed | Apr 2  | Flex                                                     |
| Fri | Apr 4  | Deep Learning                                            |
| Mon | Apr 7  | Convolution                                              |
| Wed | Apr 9  | Flex                                                     |
| Fri | Apr 11 | Festival of Scholars and Artists                         |
| Mon | Apr 14 | Autoencoders                                             |
| Wed | Apr 16 | Flex                                                     |
| Fri | Apr 18 | Generative Adversarial Networks                          |
| Mon | Apr 21 | Transformers                                             |
| Wed | Apr 23 | Large Language Models and Retrieval Augmented Generation |
| Fri | Apr 25 | Reinforcement Learning                                   |
| Mon | Apr 28 | Genetic Algorithms                                       |
| Wed | Apr 30 | Review                                                   |
| Mon | May 5  | Final presentations, 1-4 PM                              |

