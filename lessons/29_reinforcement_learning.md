# Reinforcement Learning
* Idea: Instead of giving the correct answer, give rewards (and punishments)
* Examples: Controlling a robot, playing a game
* A simulated environment can provide the rewards
  * States, actions, rewards
* Credit assignment problem: I took many actions, which were responsible for this reward?
  * Discounted sum of future rewards, so rewards farther in the future have less effect on the current action
* Temporal difference learning
  * Iteratively update the expected value of each state
  * Equation 18-4 on p. 704
  * Q-learning is similar, but updates values for state-action pairs instead of states, so you know which action to pick
* Exploration vs exploitation
  * epsilon-greedy
    * Epsilon should be decreased over the course of training so the agent behaves less randomly as it learns a good policy
* Deep Q-learning: when the set of states is too big to represent in a table
* Walk through [notebook](https://colab.research.google.com/github/ageron/handson-ml3/blob/main/18_reinforcement_learning.ipynb)