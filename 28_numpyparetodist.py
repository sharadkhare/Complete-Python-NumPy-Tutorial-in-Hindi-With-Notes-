# Pareto Dist: 80:20 ratio. (20% factors Cause 80% outcome or result)
# param - a(shape param), size
# sample for pareto dist with shape 2 with size 2*3
from numpy import random
sharad = random.pareto(a=2, size=(2,3))
print(sharad)

# visalization of pareto dist
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
sns.distplot(random.pareto(a=2, size=1000), kde=False)
plt.show()

