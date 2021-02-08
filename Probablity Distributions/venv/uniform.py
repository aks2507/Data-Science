import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
import seaborn as sns
from scipy.stats import uniform
sns.set(color_codes=True )
sns.set(rc={'figure.figsize':(5,5)})
n = 10000
start = 10
width = 20
data_uniform = uniform.rvs(size=n, loc = start, scale=width)
ax = sns.distplot(data_uniform,
                bins=100,
                kde=True,
                color='blue',
                hist_kws={"linewidth": 2,'alpha':1})
ax.set(xlabel='Uniform Distribution ', ylabel='Frequency')
plt.show()