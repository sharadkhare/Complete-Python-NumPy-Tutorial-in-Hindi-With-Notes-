#1-D Array indexing is the same as accessing an array element. strat with 0, second 1
import numpy as np
sharad = np.array([1, 2, 3, 4])
print(sharad[1])

# we can get the third and forth elements from adding them
import numpy as np
sharad = np.array([1, 2, 3, 4])
print(sharad[2] + sharad[3])

# Accessing the 2 -D - it is like a rows and columns.
import numpy as np
sharad = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
#print('2nd element in the 1st rows', sharad[0, 1])
print('5th element in the 2nd rows', sharad[1, 4])


# accessing the 3-D - same as accessing

import numpy as np
sharad = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9],[10, 11, 12 ]]])
print(sharad[0, 1, 2])