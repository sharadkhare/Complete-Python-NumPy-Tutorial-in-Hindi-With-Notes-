# Joining the numpy array - here for this we will pass concatenate()

import numpy as np
sharad = np.array([1,2,3])
sharad1 = np.array([4,5,6])
sharad2 = np.concatenate((sharad, sharad1))
print(sharad2)

# Joining of 2-D arrays along with rows(axis = 1)
import numpy as np
sharad = np.array([[1,2],[3,4]])
sharad1 = np.array([[5,6], [7,8]])
sharad2 = np.concatenate((sharad, sharad1), axis=1)
print(sharad2)

# Joining array using the stack function: 
import numpy as np
sharad = np.array([1,2,3])
sharad1 = np.array([4,5,6])
sharad2 = np.stack((sharad, sharad1), axis=1)
print(sharad2)

# Stacking along with rows: hstack()
import numpy as np
sharad = np.array([1,2,3])
sharad1 = np.array([4,5,6])
sharad2 = np.hstack((sharad, sharad1))
print(sharad2)

# Stacking along with column
import numpy as np
sharad = np.array([1,2,3])
sharad1 = np.array([4,5,6])
sharad2 = np.vstack((sharad, sharad1))
print(sharad2)

# Stacking along with height(depth)
# import numpy as np
sharad = np.array([1,2,3])
sharad1 = np.array([4,5,6])
sharad2 = np.dstack((sharad, sharad1))
print(sharad2) 