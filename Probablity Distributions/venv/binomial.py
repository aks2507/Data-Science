import matplotlib.pyplot as plt
from IPython.display import Math, Latex
import math
from IPython.core.display import Image
import seaborn as sns
from scipy.stats import binom
sns.set(color_codes=True)
sns.set(rc={'figure.figsize':(5,5)})
r_values=list(range(4,8))
dist=[]
p=0.5
for i in range(4, 8):
    a=math.factorial(i-1)*(pow(p,4)*pow(1-p,i-4) + pow(p,i-4)*pow(1-p,4))
    a=a/(6*math.factorial(i-4))
    dist.append(str(a))
    print("Probability of finishing in " + str(i) + " games is: " + str(a))
plt.bar(r_values, dist)
plt.show()
