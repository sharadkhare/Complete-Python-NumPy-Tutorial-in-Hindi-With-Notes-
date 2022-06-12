#Multinomial dist: it is a generalization of binomial dist.
# parameter - n(number of possibility or outcome), pvals(list of possibility or outcome), size(shape of returned array) 
# draw out a sample for dice roll
from numpy import random
sharad = random.multinomial(n=6, pvals=[1/6, 1/6, 1/6, 1/6, 1/6, 1/6])
print(sharad)

# multinomial samples will not produce a single value , they will produce one value for each pvals.