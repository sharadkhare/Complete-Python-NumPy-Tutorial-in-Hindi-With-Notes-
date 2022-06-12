# Iterating Array - means going through the elements one by one or step by step. like For loop.

# Iterate the element of 1-D
import numpy as np
sharad = np.array([1,2,3])
for i in sharad:
    print(i)

# Iterate 2-D
import numpy as np
sharad = np.array([[1,2,3], [4,5,6]])
for i in sharad:
    print(i)

# Iterate on each scalar element of the 2-D
import numpy as np
sharad = np.array([[1,2,3], [4,5,6]])
for i in sharad:
    for a in i:
        print(a)

# Iterate 3-D
import numpy as np
sharad = np.array([[[1,2,3], [4,5,6], [7,8,9], [10,11,12]]])
for i in sharad:
    for a in i:
        for b in a:
            print(b)

# Iterating arrays using the nditer() function.
# Now we will Iterate on each scalar element.

import numpy as np
sharad = np.array([[[1,2], [3,4], [5,6], [7,8]]])
for i in np.nditer(sharad):
    print(i)

# Now we will Iterate with different step sizes.
import numpy as np
sharad = np.array([[1,2,3,4], [5,6,7,8]])
for i in np.nditer(sharad[:, ::2]):
    print(i)

