Attendance  
Ripped From Today's Headlines

* Post-its

# Polynomial Regression
* Idea: add more features like $x^2$
  * If you have multiple features, you can include combinations: $a^2$, $ab$, $b^2$
* Overfitting is a danger (Figure 4-14)
  * How to avoid it?

# Learning Curves
* WC: What is cross-validation?
* Figure 4-15 (fitting a line to quadratic data)
  * Axes
  * What problem is evident in this learning curve?
    * How do the lines show this?
* What about Figure 4-16 (fitting a 10-degree polynomial to same data)
* Bias/variance trade-off (p. 155)
  * There are three meanings of bias
    * This one
    * Parameter 0
    * Social bias

# Regularization
* Three approaches
  * Simpler model
  * Regularization term in cost function (penalizes large weights)
    * Several variants exist
    * Why is it important to scale the data?
  * Early stopping (Figure 4-20)

# Logistic Regression
* Logistic function
  * Output is probability of classifying point as true
  * 0.5 is threshold to make a decision
* No closed-form solution, but gradient descent still works
* Decision boundaries (Figures 4-23 and 4-24)
* Softmax (when you have more than two classes)
  * Equation 4-20
  * What happens if it is given numbers that are
    * All equal
    * One significantly larger than the others
    * Two large and similar, two small and similar
* Both logistic and softmax are differentiable, which is crucial for gradient descent
  * Contrast threshold function and regular max function

* If time, work on polynomial regression assignment

* Post-its on door

# For Next Time
Read Géron, chapter 3  
First third of social context book due tomorrow  
You can now start on polynomial regression assignment
