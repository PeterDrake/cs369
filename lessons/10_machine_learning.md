Attendance
Ripped From Today's Headlines

# The Machine Learning Landscape

* Central idea: a machine learning system *learns from experience* rather than being *explicitly programmed*.
* Activity: draw cartoons for each of supervised, semisupervised, unsupervised, and reinforcement learning.
* Warm call: what's the difference between classification and regression?
  * WC: which is it if you're training a system to recognize handwritten digits?
* WC: explain the difference between instance-based and model-based learning.
  * TPS: what are the advantages of each?
* In this class we’ll mostly be talking about supervised, model-based learning.
* Training means using data to choose
a good model
  * This often means choosing *parameters* for a *family* of models.
  * Learning can be viewed as search through the family of models for a good one (or the best one).
* WC: for a classification task, how would you know if one model was better than another?
* Activity: draw pictures of overfitting and underfitting.
* WC: what is a validation set and how does it help?

# End-to-End Machine Learning Project

* Steps in a Machine Learning Project

1. Look at the big picture.
2. Get the data.
3. Discover and visualize the data to gain insights.
4. Prepare the data for Machine Learning algorithms.
5. Select a model and train it.
6. Fine-tune your model.
7. Present your solution.
8. Launch, monitor, and maintain your system.
* Note the checklist in Appendix A!

[Colab Notebooks](https://github.com/ageron/handson-ml3)

* Once you get the data, set aside a test set!
* Error metric: root mean squared error
  $$\text{RMSE}(\mathbf{X}, h) = \sqrt{\frac{1}{m} \sum_{i=1}^{m} (h(\mathbf{x}^{(i)}) - y^{(i)})^2}$$
  * See list of notations on p. 44
    * Don't panic about the linear algebra -- vectors and matrices are just 1D and 2D arrays/lists
  * Why the squaring and square root?
* Correlation
  ![Correlation](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d4/Correlation_examples2.svg/1200px-Correlation_examples2.svg.png)
* Some models we might use:
  * Line (plane / hyperplane)
  * Logistic curve
  * Polynomial
  * Decision tree
  * Random forest
  * Neural network
  * Ensemble

# For Next Time
Othello is due tonight
Read pp. 131-138
