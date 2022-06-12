# matplotlib(pyplot) -seaborn
# seaborn is a library that uses matplotlin underneath to plot graph i.r pyplot.
# Distplot - distribution plot(curve plot- histogram)

import matplotlib.pyplot as plt
import seaborn as sns 
sns.distplot([0,1,2,3,4,5])
plt.show()

# plotting a distplot without the histrogram
import matplotlib.pyplot as plt
import seaborn as sns 
x = [0,1,2,3,4,5]
sns.distplot(x, hist=False)
plt.show()