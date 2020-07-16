import copy
import random

class Hat:
    '''
    Specs say *"a hat will always be created with at least one ball"* but give no
    indication as to what kind of ball it should be.
    '''

    def __init__(self, **kwargs):
        self.contents = []
        for arg in kwargs:
            self.contents.extend(((arg + ' ') * kwargs[arg]).split(" ")[:kwargs[arg]])

        if not kwargs:
            self.contents.append(self.getSillyColorSelectionFromNothing())

    def getSillyColorSelectionFromNothing(self):
        return ["white", "purple", "grey", "green", "ored", "black", "pink", "violet"][random.randint(0, 7)]

    def draw(self, num):
        '''
        Remove num random balls from contents. Return a list of of balls removed. If num exceeds the length of
        contents, return them all.
        '''
        drawn = []
        rints = []
        for i in range(num if num < (len(self.contents)) else len(self.contents)):
            rint = random.randint(0, len(self.contents) - 1)
            drawn.append(self.contents.pop(rint))
            rints.append(rint)
        return drawn

    def resetBalls(self, balls):
        self.contents.clear()
        self.contents.extend(balls)

    def getNumBalls(self):
        return len(self.contents)


def isGreater(d1, d2):
    '''
    Determine from the keys in d1 if the values in dict d2 exist and are all >= to those in d1
    :params d1: dict<str:int> A dict with values >= 1. These are the test values to exceed.
    :params d2: dict<str:int> A dict with values >= 1. This is the tested object.
    :return: bool
    '''
    for key in d1:
        if d2.get(key, 0) < d1[key]:
            return False

    return True


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    '''
    I am not clear on the instruction for the draw method: 

        "If the number of balls to draw exceeds the available
        quantity, return all the balls."

    Does 'return all the balls' refer to  (1) return the balls from the draw method?
    That portion of the README is discussing the draw method. But it might mean
    to (2) return hat to its initial state. In regular english, the first is suggested
    but logically the second makes sense; check the results till the hat is empty or
    near empty then continue with a reset hat.

    '''
    foundit = 0
    orig = copy.deepcopy(hat.contents)
    for i in range(num_experiments):
        if hat.getNumBalls() < num_balls_drawn:
            hat.resetBalls(orig)
        drawn = hat.draw(num_balls_drawn)
        d = {}
        for ball in drawn:
            d[ball] = d.get(ball, 0) + 1
        if isGreater(expected_balls, d):
            foundit += 1
    return foundit / num_experiments
