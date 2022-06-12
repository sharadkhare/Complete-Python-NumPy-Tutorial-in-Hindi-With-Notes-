# normal(Gaussian) distribution - very important.
# random.normal() method- loc(mean), scale(standard deviation), size

# we are generating a random normal distribution of size 2*3.
from numpy import random
import numpy
sharad = random.normal(size=(2,3))
print(sharad)

# here wew ill generate a random normal dist of size 2*3 with mean at 1 and standard deviation of 2:
from numpy import random
sharad = random.normal(loc=1, scale=2,size=(2,3))
print(sharad)

# visualization of normal distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)
plt.show()

# the curve of a normal dist is also called as bell curve