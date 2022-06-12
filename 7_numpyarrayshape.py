# shape of an array - the shape of an array is the number of elements in each dimensions.
# now we will try to get the shape of any array.
import numpy as np
sharad = np.array([[1,2,3,4], [5,6,7,8]])
print(sharad.shape)

# (2,4) which means the array has 2 dimensions and it has 4 elements

# now we will create a 5-D array using ndmin :
import numpy as np
sharad = np.array([1,2,3,4], ndmin=5)
print(sharad)
print('shape of array is ', sharad.shape)