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
import random
import matplotlib.pyplot as plt


class CalculateUtility:
    __slots__ = 'NUMBER_OF_ROWS','NUMBER_OF_COLS','exploring','world','Reward','alpha', \
                'terminal_states'

    def __init__(self):
        self.NUMBER_OF_ROWS = 11
        self.NUMBER_OF_COLS = 11
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
        if col - 1 >= 1:
            result.append((row, col - 1))
        # for up action
        if row - 1 >= 1:
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
            #return self.Reward[x,y]
            return -0.004
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


def pretty_print(array):
    """
    helper funcytion to print the reward matrix nicely
    :param array:
    :return:
    """
    print("========================== print the 10 * 10 matrix ==========================")
    print()
    for row in range(1,11):
        for col in range(1,11):
            print(str(round(array[row,col],3)).ljust(5),end='\t')
        print()
    print()
    print()


def run_trials(something):
    """
    Helper function to run the required trials to calculate the reward for every grid
    :param something:
    :return:
    """
    for row in range(1,something.NUMBER_OF_ROWS):
        for col in range(1,something.NUMBER_OF_COLS):
            if (row, col) in something.terminal_states:
                continue
            something.exploring = []
            something.Reward[row, col] = something.get_reward(row, col)


def set_obstacles_in_random_places(something):
    """
    Helper function to randomly set the obstacles in the grid
    :param something:
    :return:
    """
    obstacles_to_add = 10
    while obstacles_to_add > 0:
        x = random.randint(1,10)
        y = random.randint(1,10)
        if (x,y) in something.terminal_states:
            continue
        something.terminal_states.append((x,y))
        obstacles_to_add -= 1


def single_layer_perceptron(x, theta1, y, theta2, bias):
        '''
        Calculates the output of the single perceptron by summing up the inputs
        with its associated weights and add the bias
        :param x: input one
        :param theta1: weight associated with input one
        :param y: input two
        :param theta2: weight associcated with input two
        :param bias: bias
        :return: returns the calculated output
        '''
        value = x * theta1 + y * theta2 + bias
        return value

def get_error( predicted_value,true_value):
        '''
        returns the squared error
        :param true_value:
        :param predicted_value:
        :return:
        '''
        return predicted_value - true_value


def get_learned_parameters(something):
    """
    Trains the required parameters based on the known values,
    uses 16 values to train the values
    :param something:
    :return:
    """
    learning_rate = 0.1
    # randomly assign weights
    bias = numpy.random.rand()
    theta1 = numpy.random.rand()
    theta2 = numpy.random.rand()

    for x in range(4):
        for y in range(4):
            # get the result form single perceptron
            predicted_output = single_layer_perceptron(x, theta1, y, theta2, bias)
            # get the error wrt the expected output
            error = get_error(something.Reward[x, y], predicted_output)
            # if the error is not 0 then backpropogate the error to adjust the
            # weights
            if error != 0:
                # this is the code where actual back propogation takes place and
                # the weights gets upadted
                theta1 += learning_rate * error * x
                theta2 += learning_rate * error * y
                bias += learning_rate * error * 1
    return theta1, theta2, bias


def caculate_reward_using_learned_parameter(theta1, theta2, bias, something):
    """
    Helper functions to calculate the reward for every grid based on ;linear approximation
    :param theta1:
    :param theta2:
    :param bias:
    :param something:
    :return:
    """
    for row in range(1,something.NUMBER_OF_ROWS):
        for col in range(1,something.NUMBER_OF_COLS):
            if (row, col) in something.terminal_states:
                continue

            something.Reward[row, col] = single_layer_perceptron(row, theta1, col, theta2, bias)


if __name__ == '__main__':

    # a. 10 × 10 world with a single +1 terminal state at (10,10).
    print("a. 10 × 10 world with a single +1 terminal state at (10,10).")
    something = CalculateUtility()
    # set rewards states
    something.Reward[10,10] = 1
    something.terminal_states.append((10,10))
    run_trials(something)
    pretty_print(something.Reward)


    # ==============================================================================================
    # initialise the learning rate constant

    theta1 , theta2, bias = get_learned_parameters(something)
    # 2. 10 × 10 world with a single +1 terminal state at (10,10). calculating values using least
    #  square linear approximation
    print("a. 10 × 10 world with a single +1 terminal state at (10,10) using linear approximation")
    something = CalculateUtility()
    # set rewards states
    something.Reward[10, 10] = 1
    something.terminal_states.append((10, 10))
    caculate_reward_using_learned_parameter(theta1,theta2,bias,something)
    pretty_print(something.Reward)


    #b. As in (a), but add a −1 terminal state at (10,1).
    print("b. As in (a), but add a −1 terminal state at (10,1).")
    something = CalculateUtility()
    # set rewards states
    something.Reward[10, 10] = 1
    something.Reward[10, 1] = -1
    something.terminal_states.append((10, 10))
    something.terminal_states.append((10, 1))
    run_trials(something)
    pretty_print(something.Reward)

    # ==============================================================================================
    # initialise the learning rate constant

    # b. As in (a), but add a −1 terminal state at (10,1).
    print("b. As in (a), but add a −1 terminal state at (10,1) using linear approximation")
    something = CalculateUtility()
    # set rewards states
    something.Reward[10, 10] = 1
    something.Reward[10, 1] = -1
    something.terminal_states.append((10, 10))
    something.terminal_states.append((10, 1))
    caculate_reward_using_learned_parameter(theta1, theta2, bias, something)
    pretty_print(something.Reward)


    # c. As in (b), but add obstacles in 10 randomly selected squares
    print("c. As in (b), but add obstacles in 10 randomly selected squares")
    print("Value showing 0 is the obstacles")
    something = CalculateUtility()
    # set rewards states
    something.Reward[10, 10] = 1
    something.Reward[10, 1] = -1
    something.terminal_states.append((10, 10))
    something.terminal_states.append((10, 1))
    set_obstacles_in_random_places(something)
    run_trials(something)
    pretty_print(something.Reward)

    # ==============================================================================================
    # initialise the learning rate constant

    # c. As in (b), but add obstacles in 10 randomly selected squares
    print("c. As in (b), but add obstacles in 10 randomly selected squares using linear square "
          "approximation")
    print("Value showing 0 is the obstacles")
    something = CalculateUtility()
    # set rewards states
    something.Reward[10, 10] = 1
    something.Reward[10, 1] = -1
    something.terminal_states.append((10, 10))
    something.terminal_states.append((10, 1))
    set_obstacles_in_random_places(something)
    caculate_reward_using_learned_parameter(theta1, theta2, bias, something)
    pretty_print(something.Reward)

    # d.As in (b), but place a wall stretching from (5,2) to (5,9).
    print("d.As in (b), but place a wall stretching from (5,2) to (5,9).")
    something = CalculateUtility()
    # set rewards states
    something.Reward[10, 10] = 1
    something.Reward[10, 1] = -1
    something.terminal_states.append((10, 10))
    something.terminal_states.append((10, 1))
    for _ in range(2,10):
        something.terminal_states.append((5,_))
    run_trials(something)
    pretty_print(something.Reward)
    # plt.imshow(something.Reward, cmap='hot', interpolation='nearest')
    # plt.show()

    # ==============================================================================================
    # initialise the learning rate constant

    # d.As in (b), but place a wall stretching from (5,2) to (5,9).
    print("d.As in (b), but place a wall stretching from (5,2) to (5,9)  using linear square ")
    something = CalculateUtility()
    # set rewards states
    something.Reward[10, 10] = 1
    something.Reward[10, 1] = -1
    something.terminal_states.append((10, 10))
    something.terminal_states.append((10, 1))
    for _ in range(2, 10):
        something.terminal_states.append((5, _))
    caculate_reward_using_learned_parameter(theta1, theta2, bias, something)
    pretty_print(something.Reward)
    # plt.imshow(something.Reward, cmap='hot', interpolation='nearest')
    # plt.show()



    #e. As in (a), but with the terminal state at (5,5).

    print("e. As in (a), but with the terminal state at (5,5).")
    something = CalculateUtility()
    # set rewards states
    something.Reward[10, 10] = 1
    something.Reward[5, 5] = 1
    something.terminal_states.append((10, 10))
    run_trials(something)
    pretty_print(something.Reward)

    # ==============================================================================================
    # initialise the learning rate constant

    print("e. As in (a), but with the terminal state at (5,5)  using linear square ")
    something = CalculateUtility()
    # set rewards states
    something.Reward[10, 10] = 1
    something.Reward[5, 5] = 1
    something.terminal_states.append((10, 10))
    caculate_reward_using_learned_parameter(theta1, theta2, bias, something)
    pretty_print(something.Reward)







    

