__author__ = 'Ketan Kokane'

"""
CSCI 630 : Foundations of Intelligent System
The code calculates the true reward utility function of the for a reinforcement agent 
The code uses Bellman's equation to calculate the rewards of each grid position 
the code calculates the values of 5 different world prints its value 
and then uses least square linear approximation to calculate the approximate value
of each grid instead of actually calculating
"""

import numpy


class CalculateUtility:
    __slots__ = 'NUMBER_OF_ROWS','NUMBER_OF_COLS','exploring','world','Reward','alpha', \
                'terminal_states'

    def __init__(self):
        self.NUMBER_OF_ROWS = 10
        self.NUMBER_OF_COLS = 10
        self.Reward = numpy.zeros((self.NUMBER_OF_ROWS, self.NUMBER_OF_COLS))
        self.exploring = []
        self.alpha = 0.9
        self.terminal_states = []

    def neighbors_of(self, row, col):
        """
        gets the neighboring states of the given state based on the actions
        that can be provided on them
        :param row:
        :param col:
        :return:
        """
        if (row,col) in self.terminal_states:
            return []
        result = []
        # for right action
        if col + 1 < self.NUMBER_OF_COLS:
            result.append((row, col + 1))
        # for left action
        if col - 1 >= 0:
            result.append((row, col - 1))
        # for up action
        if row - 1 >= 0:
            result.append((row-1,col))
        # for down action
        if row + 1 < self.NUMBER_OF_ROWS:
            result.append((row+1,col))
        return result

    def get_reward(self, x, y):
        """
        recursively calculates the reward of each position in the grid
        using the bellman's equation, by iterating all the states which
        can be reached from the current state using all the possible actions
        :param x: x co ordinate of the current position
        :param y: y co ordinate of the current position
        :return: discounted reward
        """
        if (x,y) in self.exploring:
            return self.Reward[x,y]
        if self.Reward[x,y] != 0:
            return self.Reward[x, y]
        self.exploring.append((x,y))
        neighbors = self.neighbors_of(x,y)
        result = []
        for neighbor in neighbors:
            if neighbor not in self.exploring:
                result.append(self.get_reward(neighbor[0], neighbor[1]))
        self.exploring.remove((x,y))
        if len(result) > 0:
            self.Reward[x,y] = self.Reward[x, y] + self.alpha * numpy.max(result)
        return self.Reward[x,y]

if __name__ == '__main__':
    # A
    something = CalculateUtility()
    # set rewards states
    something.Reward[9,9] = 1
    something.terminal_states.append((9,9))
    for row in range(something.NUMBER_OF_ROWS):
        for col in range(something.NUMBER_OF_COLS):
            something.exploring = []
            something.Reward[row, col] = something.get_reward(row, col)
    print(something.Reward)

