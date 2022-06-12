# Chi Square Dist: it is basically used as a basis to verify the hypothesis.
# param - df(degree of freedom), size

# sample for chi squared dist with df 2 with size 2*3
from numpy import random
sharad = random.chisquare(df=2, size=(2,3))
print(sharad)

# visualization of chi square.
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.chisquare(df=1, size=1000), hist=False)
plt.show()