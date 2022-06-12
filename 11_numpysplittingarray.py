# spliting arrays in numpy- it is reverse to joining, breaking the array.
# array_split()

# split the array in 3 parts:
import numpy as np
sharad = np.array([1,2,3,4,5,6])
sharadnew = np.array_split(sharad, 3)
print(sharadnew)

# now we will split this array in 4 parts
import numpy as np
sharad = np.array([1,2,3,4,5,6])
sharadnew = np.array_split(sharad, 4)
print(sharadnew)

# split into array with index

import numpy as np
sharad = np.array([1,2,3,4,5,6])
sharadnew = np.array_split(sharad, 3)
print(sharadnew[0])
print(sharadnew[1])
print(sharadnew[2])


# splitting the 2-D array
import numpy as np
sharad = np.array([[1,2], [3,4], [5,6], [7,8], [9,10], [11,12]])
sharadnew = np.array_split(sharad, 3)
print(sharadnew)

# split the 2-D array into three 2-D arrays
import numpy as np
sharad = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
sharadnew = np.array_split(sharad, 3)
print(sharadnew)

# spliting the 2-D into three 2-Dalong with rows
import numpy as np
sharad = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
sharadnew = np.array_split(sharad, 3, axis=1)
print(sharadnew)

#alternate solution is using the hsplit(), opposite hstack()
import numpy as np
sharad = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12], [13,14,15], [16,17,18]])
sharadnew = np.hsplit(sharad, 3)
print(sharadnew)