import numpy
import random

# CONSTANTS 
BAR = 'BAR'
BELL = 'BELL'
LEMON = 'LEMON'
CHERRY = 'CHERRY'
POSSIBLE_SYMBOLS = [BAR, BELL, LEMON, CHERRY]


def getRandomNumber():
    # generate a random number between 0 to 3 with the given equal probabilities 
    # then map the generated number to one of the symbol that can be seen on the slot machine
    return POSSIBLE_SYMBOLS[numpy.random.choice(numpy.arange(0, 4), p=[0.25, 0.25, 0.25, 0.25])]


def simulation(initialAmount = 10):
    """
    runs the simulation
    :param initialAmount:
    :return: returns the number of plays made by the player till the coins
    ran out
    """
    # initialise the number of plays
    numberOfPlays = 0
    # continue till you are broke
    while initialAmount > 0:
        # insert coin in the machine to play it
        initialAmount -= 1
        # pull the slot machine and get the configuration it gives
        # e.g. BARBARBAR
        configuration = pullSlotMachineLever()
        #get the rewards based on the current configuartion
        initialAmount += coinsEarned(configuration)
        # keep count of the number of plays made by the player
        numberOfPlays +=1 
    return numberOfPlays


def pullSlotMachineLever():
    #  get the symbol on the left wheel
    left = getRandomNumber()
    #  get the symbol on the middle wheel
    middle = getRandomNumber()
    #  get the symbol on the right wheel
    right = getRandomNumber()
    # add up all the configuration from each wheel to form the main
    # configuration
    configuration = left + middle + right 
    return configuration


def coinsEarned(configuration):
    """
    used the given conditions to decide the payback for each configuration
    :param configuration:
    :return:
    """
    if configuration == BAR * 3:
        # if BARBARBAR is the configruation return 20 coins
        return 20

    elif configuration == BELL * 3:
        # is 3 BELLS
        return 15

    elif configuration == LEMON * 3:
        return 5

    elif configuration == CHERRY *3:
        return 3

    elif configuration[:len(CHERRY)*2] == CHERRY*2:
        # if CHERRYCHERRY_______ then return 2 coins
        return 2

    elif configuration[:len(CHERRY)] == CHERRY:
        # if CHERRY_____________ then return 1 coin
        return 1

    else:
        # if none of the above configuration then return 0 coin
        return 0


if __name__ == "__main__":
    # initailiase a list
    numberOfTimesPlayed = []
    # run the simulation for 100 times 
    for _ in range(100):
        # append result of every simulation in the list
        numberOfTimesPlayed.append(simulation())
    # convert the list to numpy array to calculate mean and median of the number of times the gambler played 
    numpyArray = numpy.array(numberOfTimesPlayed)
    print('mean',numpy.mean(numpyArray))
    print('median',numpy.median(numpyArray))
    print('minimum',numpy.min(numpyArray))
    print('maximum',numpy.max(numpyArray))