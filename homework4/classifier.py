__author__ = 'ketan kokane'
'''
program to code a single layer perceptron to do binary classfication for the 
given dataset. The required dataset is hard coded in the list. The tarining 
part of the code initialises the weights of the network randomly, then after 
each example based on the error back propogates the error and updates each 
weight in aim of reducing the error. To calculate the error of each weight 
took partial derivate of the output.
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
    '''
    Helper function which prints the given attributes, with simple
    beautificatino trick
    :param w1:
    :param w2:
    :param b:
    :return:
    '''
    print(str(w1).ljust(20),str(w2).ljust(20),str(b).ljust(20))


def train_neuron(dataset, verbose):
    '''
    function to train a neuron
    :param dataset:
    :param verbose: used to decide if the print statements are required or no
    :return:
    '''
    # initialise the learning rate constant
    learning_rate = 0.1
    # randomly assign weights
    b = numpy.random.rand()
    w1 = numpy.random.rand()
    w2 = numpy.random.rand()
    if verbose:
        print("W1".ljust(20), "W2".ljust(20), "bias".ljust(20))

    print_parameters(w1, w2, b)
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
            # this is the code where actual back propogation takes place and
            # the weights gets upadted
            w1 += learning_rate * error * weight
            w2 += learning_rate * error * length
            b += learning_rate * error * 1
        # print(true_ouput, predicted_output)
        if verbose:
            print_parameters(w1, w2, b)

    return w1, w2, b


def test_neuron(dataset,w1, w2, b):
    '''
    tests the single layer perceptron with the given data set and weights
    :param dataset:
    :param w1:
    :param w2:
    :param b:
    :return:
    '''
    for weight, length, true_ouput in dataset:
    # get the result form single perceptron
        predicted_output = single_layer_perceptron(weight, w1, length, w2, b)
    # get the output as Either 0 or 1
        predicted_output = threshold(predicted_output)
    # get the error wrt the expected output
        print('expected output for Weight %d and length %d = %d and predicted output = %d'% (weight, length, true_ouput, predicted_output))




def main():
    # get the required dataset
    dataset = initialise()
    # train the model on all the data points to see if the dataset converges
    # the model
    train_neuron(dataset, verbose=True)

    # train the model with only 6 data points and two data points for testing
    w1, w2, b = train_neuron(dataset[:6], verbose=False)
    print()
    print()
    print('Testing the neuron with two unseen data points')
    print()
    # now test the model based on the learned weights
    test_neuron(dataset[-2:],w1, w2, b)



if __name__ == '__main__':
    main()
