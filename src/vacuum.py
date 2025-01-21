import random
import tkinter as tk
import statistics

OFFSETS = {'north': (0, 1), 'east': (1, 0), 'south': (0, -1), 'west': (-1, 0)}


def generate_world(width):
    def f():
        r = random.random()
        if r < 0.05:
            return 'wall'
        elif r < 1.0:
            return 'dirt'
        else:
            return 'clear'
    return [[f() for _ in range(width)] for _ in range(width)]


def place_agent(world):
    width = len(world)
    while True:
        x = random.randrange(width)
        y = random.randrange(width)
        if world[x][y] != 'wall':
            return x, y


def vector_sum(p, q):
    return tuple([a + b for a, b in zip(p, q)])


def take_action(world, agent, agent_function):
    x, y = agent
    width = len(world)
    action = agent_function(world[x][y] == 'dirt')
    if action == 'clean':
        world[x][y] = 'clean'
        return agent
    else:
        x, y = vector_sum(agent, OFFSETS[action])
        if 0 <= x < width and 0 <= y < width and world[x][y] != 'wall':
            return x, y
        else:
            return agent


def count_dirt(world):
    width = len(world)
    result = 0
    for x in range(width):
        for y in range(width):
            if world[x][y] == 'dirt':
                result += 1
    return result


def setup_animation(agent, width, world):
    square_width = 400 // width
    root = tk.Tk()
    root.title('Vacuum world')
    canvas = tk.Canvas(root, width=width * square_width, height=width * square_width)
    canvas.pack()
    marks = [[None] * width for _ in range(width)]
    for x in range(width):
        for y in range(width):
            s = world[x][y]
            if s == 'wall':
                canvas.create_rectangle(x * square_width,
                                        (width - 1 - y) * square_width,
                                        (x + 1) * square_width,
                                        (width - y) * square_width,
                                        fill='blue',
                                        outline='')
            elif s == 'dirt':
                marks[x][y] = canvas.create_oval((x + 0.1) * square_width,
                                                 (width - y - 1 + 0.1) * square_width,
                                                 (x + 0.9) * square_width,
                                                 (width - y - 1 + 0.9) * square_width,
                                                 fill='tan',
                                                 outline='')
    x, y = agent
    agent_circle = canvas.create_oval(x * square_width,
                                      (width - 1 - y) * square_width,
                                      (x + 1) * square_width,
                                      (width - y) * square_width, fill='black')
    return root, canvas, marks, agent_circle, square_width


def run(width, steps, agent_function, agent_reset_function=lambda : None, animate=True):
    agent_reset_function()
    world = generate_world(width)
    agent = place_agent(world)
    loss = 0
    if animate:
        def animate_step():
            nonlocal agent
            nonlocal loss
            nonlocal steps
            oldx, oldy = agent
            agent = take_action(world, agent, agent_function)
            x, y = agent
            loss += count_dirt(world)
            canvas.move(agent_circle, (x - oldx) * square_width, (oldy - y) * square_width)
            if world[x][y] == 'clean' and marks[x][y] is not None:
                canvas.delete(marks[x][y])
                marks[x][y] = None
            steps -= 1
            if steps > 0:
               canvas.after(100, animate_step)
            else:
                print('Loss: ', loss)
        root, canvas, marks, agent_circle, square_width = setup_animation(agent, width, world)
        animate_step()
        root.mainloop()
    else:
        for i in range(steps):
            agent = take_action(world, agent, agent_function)
            loss += count_dirt(world)
        return loss


def many_runs(width, steps, runs, agent_function, agent_reset_function=lambda : None):
    return statistics.mean([run(width, steps, agent_function, agent_reset_function, False) for i in range(runs)])
