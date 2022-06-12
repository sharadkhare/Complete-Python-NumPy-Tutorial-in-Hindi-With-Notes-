# Rayleigh Dist: it is used in signal processing.
# param - scale(standarad deviation, how flat the distribution is .. default 1.0), size

# sample for Rl with scale of 2.0 with size of 2*3
from numpy import random
sharad = random.rayleigh(scale=2, size=(2,3))
print(sharad)

# visualization of Rayleigh dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.rayleigh(size=1000), hist=False)
plt.show()