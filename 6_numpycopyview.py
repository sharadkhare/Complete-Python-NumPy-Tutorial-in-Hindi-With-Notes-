# difference between numpy array copy and view.
# we will make a copy, change in original array, and display both.

import numpy as np
sharad = np.array([1,2,3,4,5])
sharad1 = sharad.copy()
sharad1[0] = 12
print(sharad)
print(sharad1)

# now we will make a view, change original, display both

import numpy as np
sharad = np.array([1,2,3,4,5])
sharad1 = sharad.view()
sharad[0] = 31
print(sharad)
print(sharad1)
