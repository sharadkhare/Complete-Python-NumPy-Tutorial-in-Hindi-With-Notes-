'''# binomial dist - discrete dist- binary output.
# param - n(number of trials), p(probability), size(shape-returned array)

# given 10 trial for a coin which will generate 10 data points:

from numpy import random
sharad = random.binomial(n=10, p=0.5, size=10)
print(sharad)

# visualization of binomial dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.binomial(n=10, p=0.5, size=1000), hist=True, kde=False)
plt.show()'''

# Difference between noemal and binomial- normal(continues) and binomial(discrete)
# i use 500 data point for binomial and under 100 data point for normal dist.

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.normal(loc=50, scale=5, size=1000), hist=False, label='Normal')
sns.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='Binomial')
plt.show()