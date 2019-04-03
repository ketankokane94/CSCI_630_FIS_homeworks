__author__ = 'ketan kokane'
'''

'''

import numpy


def single_layer_perceptron(input1, w1, input2, w2, b):
    '''
    Calculates the output of the single perceptron by summing up the inputs
    with its associated weights and add the bias
    :param input1: input one
    :param w1: weight associated with input one
    :param input2: input two
    :param w2: weight associcated with input two
    :param b: bias
    :return: returns the calculated output
    '''
    x = input1 * w1 + input2 * w2 + b
    return x


def get_error(true_value, predicted_value):
    '''
    Simply returns the the expected true value - the value predicted by the
    neuron
    :param true_value:
    :param predicted_value:
    :return:
    '''
    return true_value - predicted_value


def threshold(predicted):
    '''
    As the neuron is expected to do binary classfication, the function
    returns either 0 or 1 based on the set threshold value
    threshold value = 0
    :param predicted:
    :return:
    '''
    if predicted > 0:
        return 1
    else:
        return 0


def initialise():
    '''
    Initialises the dataset that is to be used by the network

    :return:
    '''
    # initialse the weights based on given data
    WEIGHTS = [11, 35, 21, 60, 37, 26, 44, 12]
    # initialse the lengths of the aligator based on the given data
    LENGTH = [70, 11, 45, 80, 32, 64, 30, 60]
    # if the aligator is from TEXAS = 1, else if from FLORIDA = 0
    LABEL = [1, 0, 1, 0, 0, 1, 0, 1]
    # combined the three seperate lists into one list and return
    dataset = list(zip(WEIGHTS, LENGTH, LABEL))

    return dataset


def print_parameters(w1, w2, b):
    print(str(w1).ljust(20),str(w2).ljust(20),str(b).ljust(20))


def main():
    dataset = initialise()
    # initialise the learning rate constant
    learning_rate = 0.1
    # randomly assign weights
    b = numpy.random.rand()
    w1 = numpy.random.rand()
    w2 = numpy.random.rand()

    print("W1".ljust(20), "W2".ljust(20),"bias".ljust(20))

    print_parameters(w1,w2,b)
    for weight, length, true_ouput in dataset:
        # get the result form single perceptron
        predicted_output = single_layer_perceptron(weight, w1, length, w2, b)
        # get the output as Either 0 or 1
        predicted_output = threshold(predicted_output)
        # get the error wrt the expected output
        error = get_error(true_ouput, predicted_output)
        # if the error is not 0 then backpropogate the error to adjust the
        # weights
        if error != 0:
            #this is the code where actual back propogation takes place and
            # the weights gets upadted
            w1 += learning_rate * error * weight
            w2 += learning_rate * error * length
            b += learning_rate * error * 1
        #print(true_ouput, predicted_output)
        print_parameters(w1, w2, b)


if __name__ == '__main__':
    main()
