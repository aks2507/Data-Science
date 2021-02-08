import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
import seaborn as sns
sns.set(color_codes=True )
sns.set(rc={'figure.figsize':(5,5)})
from scipy.stats import gamma
data_gamma = gamma.rvs(a=5, size=10000)
ax = sns.distplot(data_gamma,
                  kde=True ,
                  bins=100,
                  color='skyblue',
                  hist_kws={"linewidth": 2,'alpha':1})
ax.set(xlabel='Gamma Distribution', ylabel='Frequency')
plt.show()