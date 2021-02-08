import math
from scipy.stats import poisson
from numpy import random
import seaborn as sns
import matplotlib.pyplot as plt

def poisson_pdf(lb, k):
    return (math.pow(lb, k) * math.exp(-lb)) / math.factorial(k)

errors=905
pres=289411
test_range=10
mean=test_range*(errors/pres)
print("Required Probability = ",(1 - math.exp(-mean)))
print(mean)

r_values=list(range(10))
dist=[]
for i in range(10):
    dist.append(poisson_pdf(mean,i))
    print(poisson_pdf(mean,i))
plt.bar(r_values,dist)
plt.show()
