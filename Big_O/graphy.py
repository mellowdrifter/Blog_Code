import matplotlib.pyplot as pyplot
import numpy as np


def graph(x, y, title, filename):
    '''x and y are lists of values'''
    pyplot.figure(figsize=(7, 5))
    x = np.array(x)
    y = np.array(y)
    pyplot.plot(x, y, 'o-', linewidth = 2)
    pyplot.title(title)
    pyplot.xlabel('Input Size')
    pyplot.ylabel('Run Time')
    pyplot.grid(True)
    pyplot.savefig(filename + ".png")
    pyplot.show()
