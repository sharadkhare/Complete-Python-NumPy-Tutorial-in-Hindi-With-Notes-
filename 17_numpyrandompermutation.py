# Permutation refers to an arrangement of elements like [3,2,1] is permutation of [1,2,3] and vice versa.
# the numpy random module provides 2 methods: shuffle() and permutation().

# shuffle() method make changes to the original array 
# now we will randomly suffle elemements for the below array:
from numpy import random
import numpy as np
sharad = np.array([1,2,3,4,5])
random.shuffle(sharad)
print(sharad)

# now we will generate a permutation of elements for the below array:
# the permutation() method leaves the original array unchanged.
from numpy import random
import numpy as np
sharad = np.array([1,2,3,4,5])
print(random.permutation(sharad)) 
 