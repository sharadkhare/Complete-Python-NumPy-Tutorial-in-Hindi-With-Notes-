# summations: difference: addition is done between 2 arguments whereas summation happens over n elements.

# adding the 2 array.
import numpy as np
sharad1 = np.array([1,2,3])
sharad2 = np.array([1,2,3])
sharadnew = np.add(sharad1, sharad2)
print(sharadnew)

# sum the values in 2 array:
import numpy as np
sharad1 = np.array([1,2,3])
sharad2 = np.array([1,2,3])
sharadnew = np.sum([sharad1, sharad2])
print(sharadnew)

# summation over an axis: if you specify axis=1, numpy will sum the number in each array.

import numpy as np
sharad1 = np.array([1,2,3])
sharad2 = np.array([1,2,3])
sharadnew = np.sum([sharad1, sharad2], axis=1)
print(sharadnew)

# cummulative sum: means partially adding thr element in array.
# example: [1,2,3,4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1,3,6,10] represent by cumsum()
import numpy as np
sharad = np.array([1,2,3])
sharadnew = np.cumsum(sharad)
print(sharadnew)