Attendance  
Ripped From Today's Headlines

# TensorFlow
* Keras is the front end for TensorFlow; they used to be separate
* Basic idea:
  * Use Python to describe your model and hyperparameters (e.g., learning rate)
  * Compile model into efficient C++ code
  * Run the model
* ReLU (Rectified Linear Unit): $max(0, z)$
* [Notebook from textbook](https://colab.research.google.com/github/ageron/handson-ml3/blob/main/10_neural_nets_with_keras.ipynb), from "Implementing MLPs in Keras" through "Building a Regression MLP Using the Sequential API"
* [A cautionary tale about data snooping](https://www.youtube.com/watch?v=EZBUDG12Nr0&t=3102s) 51:42-58:48
    ```python
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_valid = scaler.transform(X_valid)
    X_test = scaler.transform(X_test)
    ```
* APIs for building networks
  * Sequential (when you just have a stack of layers)
  * Functional (when your layers have a more complex arrangement)
  * Subclassing (when you want to do something extremely unusual)
* Saving and restoring
  * You can save the state of a model, so you can run the trained model later
    * Many systems are built on models previously trained by others
  * Checkpointing
  * Early stopping
* Tuning hyperparameters
  1. Write a function to build your model
  2. Pass that function to KerasRegressor
  3. Pass that to RandomizedSearchCV
  * Several other techniques exist, including evolutionary algorithms
* Hyperparameter advice
  * Hidden layers: “ramp up the number of hidden layers until you start overfitting”.
  * Neurons per layer: “same number of neurons in all hidden layers”, “more layers and neurons than you actually need”
  * Learning rate: trial and error
  * Optimizer: see chapter 11
  * Batch size: 32?
  * Activation function: ReLU
