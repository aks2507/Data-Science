import matplotlib.pyplot as plt
from IPython.display import Math, Latex
from IPython.core.display import Image
import seaborn as sns
from scipy.stats import norm
sns.set(color_codes=True )
sns.set(rc={'figure.figsize':(5,5)})
data_normal = norm.rvs(size=10000,loc=0,scale=1)

ul=norm(loc=0,scale=1).cdf(2.07)
ll=norm(loc=0,scale=1).cdf(0)
print("0 <= Z <= 2.07:",(ul-ll))

ul=norm(loc=0,scale=1).cdf(-0.11)
ll=norm(loc=0,scale=1).cdf(-0.64)
print("-0.64 <= Z <= -0.11: ",(ul-ll))

ll=norm(loc=0,scale=1).cdf(-1.06)
print("Z >= -1.06: ",(1-ll))

print("Z <= -2.33: ",norm(loc=0,scale=1).cdf(-2.33))

ll=norm(loc=0,scale=1).cdf(4.61)
print("Z >= -4.61: ",(1-ll))

ax = sns.distplot(data_normal,
                  bins=100,
                  kde=True ,
                  color='skyblue',
                  hist_kws={"linewidth": 2,'alpha':1})
ax.set(xlabel='Normal Distribution', ylabel='Frequency')
plt.show()
