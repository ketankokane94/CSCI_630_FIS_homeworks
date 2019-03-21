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
    numberOfPlays = 0
    while initialAmount > 0:
        configuration = pullSlotMachineLever()
        initialAmount -= 1
        initialAmount += coinsEarned(configuration)
        numberOfPlays +=1 
    return numberOfPlays

def pullSlotMachineLever():
    left = getRandomNumber()
    middle = getRandomNumber()
    right = getRandomNumber()
    configuration = left + middle + right 
    return configuration

def coinsEarned(configuration):
    if configuration == BAR * 3:
        return 20
    elif configuration == BELL * 3:
        return 15
    elif configuration == LEMON * 3:
        return 5
    elif configuration == CHERRY *3:
        return 3
    elif configuration[:len(CHERRY)*2] == CHERRY*2:
        return 2
    elif configuration[:len(CHERRY)] == CHERRY:
        return 1
    else:
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