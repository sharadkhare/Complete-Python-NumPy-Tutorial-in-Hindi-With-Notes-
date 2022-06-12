# Zipf Dist: its defination is like.. common word in english has occurs nearly 1/5 time as of the most hindi words
# param - a(dist param), size
# sample for zipf dist with a as 2 with size 2*3
from numpy import random
sharad = random.zipf(a=2, size=(2,3))
print(sharad)

# visualization of zipf dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sharad = random.zipf(a=2, size=1000)
sns.distplot(sharad[sharad<10], kde=False)
plt.show() 

