import math
import pandas as pd
import matplotlib.pyplot as plt


P_h1 = 0.1
P_h2 = 0.2
P_h3 = 0.4
P_h4 = 0.2

P_lime_given_h1 = 0
P_lime_given_h2 = 0.25
P_lime_given_h3 = 0.5
P_lime_given_h4 = 0.75

hypothesis = []
hypothesis.append((P_h1,P_lime_given_h1))
hypothesis.append((P_h2,P_lime_given_h2))
hypothesis.append((P_h3,P_lime_given_h3))
hypothesis.append((P_h4,P_lime_given_h4))

result = []
for h_i in hypothesis:
    r = []
    for observation in range(0, 101):
        r.append(math.pow(h_i[1], observation) * h_i[0])
    result.append(r)

data = pd.DataFrame({'h1':result[0],'h2':result[1],'h3':result[2],'h4':result[3]})
data.plot(figsize=(12,8))
plt.show()