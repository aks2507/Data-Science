import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
import seaborn as sns
sns.set(color_codes=True )
sns.set(rc={'figure.figsize':(5,5)})
from scipy.stats import bernoulli
data_bern = bernoulli.rvs(size=10000,p=0.6)
ax= sns.distplot(data_bern,
                 kde=False ,
                 color="skyblue",
                 hist_kws={"linewidth": 2,'alpha':1})
ax.set(xlabel='Bernoulli Distribution', ylabel='Frequency')
plt.show()