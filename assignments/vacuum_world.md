# Overview
This assignment asks you to experiment with programming a simulated robot vacuum cleaner. It is not meant to exercise any particular AI technique, but rather to give you a chance to come up with your own techniques, confront a challenging environment, and practice your Python.

**This is an individual assignment. You are meant to write the code on your own. You are welcome to discuss *ideas* with other students (including on the class email list), but don't look at their code or show them yours.**

# Files
* [vacuum.py](../src/vacuum.py)

# The Vacuum World

The vacuum world is a two-dimensional grid of spaces. Each space either contains an impassable wall, is dirty, or is clean. The agent (the simulated vacuum cleaner) is dropped into a random non-wall space. Its task is to clean up the world as quickly as possible. This is measured by “loss”; in each step of the simulation, the agent’s loss increases by the number of spaces in the world that are still dirty.

In each step, the agent receives a boolean percept. This is `True` if it is in a dirty space, `False` otherwise. The agent chooses one of the following actions:
* `'clean'` (clean the current space)
* `'north'` (move north)
* `'east'` (move east)
* `'south'` (move south)
* `'west'` (move west)

If the agent cleans while in a dirty space, that space becomes clean. Cleaning a clean space has no effect. Moving moves to an adjacent space in the specified direction, unless that would move the agent into a wall or off the edge of the world; in that case, the action has no effect.

The agent does not know where it is, where the walls are, or whether its move actions have succeeded! The only thing it can sense is whether the current space is dirty.

The agent is defined as a function, which takes the percept as an argument and returns the action.

# Your Agents
## Reflex Agent
The reflex agent receives a percept and returns an action, with no randomness or memory. This is extremely ineffective, but easy to implement with an if statement.

Provide a function `reflex_agent`, which takes a boolean percept as an argument.

## Random Agent
The random agent also has no memory, but can act randomly. Surprisingly, this can be more effective than the reflex agent.

You will want to import the random package at the beginning of your file and use methods like random.choice. For example, given the definition of directions above, random.choice(directions) returns a random element of that list.

This function should be called `random_agent`

## State Agent
The state agent is allowed to remember what it has seen and done in the past. This allows it to perform even better than the random agent.

This function should be called `state_agent`.

To behave differently each time it is called, your state agent function will need to have some variables whose values are remembered between calls. One way to do this is to define these variables at the top (global) level, then use the `global` keyword to modify them within your agent function.

# Testing Your Agents

If you have

`from vacuum import *`

at the top of your file, you can see your reflex agent in action with this statement:

`run(20, 50000, reflex_agent)`

This makes a 20x20 world and runs it for 50 000 steps.

Alternatively, to run this experiment 10 times without the animation and see the average loss:

`print(many_runs(20, 50000, 10, reflex_agent))`

Your state agent may include a second function whose job it is to reset the global variables to their initial values. You would test that with statements like

`run(20, 50000, state_agent, state_agent_reset)`

and:

`print(many_runs(20, 50000, 10, state_agent, state_agent_reset))`

My solution got average losses of around 19 000 000 for the reflex agent, 630 000 for the random agent, and 380 000 for the state agent. Maybe you can do even better!

# What to Hand in
Hand in your file `vacuum_agents.py` that contains your function definitions and any global variable definitions.
