__author__ = 'Ketan Kokane'

"""
CSCI 630 Foundations of Intelligent systems
the code calculates the probabilities of every hypothesis given 100 lime data point and 
also shows the probability of of nth + 1 being a lime
"""
import math
import pandas as pd
import matplotlib.pyplot as plt


# probability of hypothesis h1
P_h1 = 0.1
# probability of hypothesis h2
P_h2 = 0.2
# probability of hypothesis h3
P_h3 = 0.4
# probability of hypothesis h4
P_h4 = 0.2

# probabilty of lime given hypothesis h1
P_lime_given_h1 = 0
# probabilty of lime given hypothesis h2
P_lime_given_h2 = 0.25
# probabilty of lime given hypothesis h3
P_lime_given_h3 = 0.5
# probabilty of lime given hypothesis h4
P_lime_given_h4 = 0.75

# array to store the data about all the hypothesis
hypothesis = []
hypothesis.append((P_h1,P_lime_given_h1))
hypothesis.append((P_h2,P_lime_given_h2))
hypothesis.append((P_h3,P_lime_given_h3))
hypothesis.append((P_h4,P_lime_given_h4))

result = []
estimation = []
# for every hypothesis
for h_i in hypothesis:
    r = []
    estimate = []
    # for every picked limes
    for observation in range(0, 101):
        # calculate the probability of data coming from every hypothesis
        r.append(math.pow(h_i[1], observation) * h_i[0])
        # Calculate the probability of next pick would be a lime from selected hypothesis
        estimate.append(h_i[1] * math.pow(h_i[1], observation) * h_i[0])
    estimation.append(estimate)
    result.append(r)

data = pd.DataFrame({'h1':result[0],'h2':result[1],'h3':result[2],'h4':result[3]})
data1 = pd.DataFrame({'h1':estimation[0],'h2':estimation[1],'h3':estimation[2],'h4':estimation[3]})
data.plot(figsize=(12,8),title='Probability of hi being the hypothesis given the data')
data1.plot(figsize=(12,8),title='Estimation of Nth being the lime given N-1 where lime')

plt.show()