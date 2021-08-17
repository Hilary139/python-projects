#piechart with python

import matplotlib.pyplot as plt

s = [50, 20, 10, 10, 10]
l = ['python', 'java', 'c++', 'swift', 'javascript']

plt.pie(s, labels=l)
plt.show()
