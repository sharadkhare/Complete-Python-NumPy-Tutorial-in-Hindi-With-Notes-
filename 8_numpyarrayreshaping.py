# reshaping - means changing the shape of an array ,like adding or removing the elements.

# reshaping from 1-D to 2-D
import numpy as np
sharad = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
sharad1 = sharad.reshape(4, 3)
print(sharad1)

# reshping from 1-D to 3-D
import numpy as np
sharad = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
sharad1 = sharad.reshape(2, 3, 2)
print(sharad1)

# Return copy or view
import numpy as np
sharad = np.array([1,2,3,4,5,6,7,8])
print(sharad.reshape(2, 4).base)

# unknown dimension - you are only allowed to have one unknown dimension. pass -1.

import numpy as np
sharad = np.array([1,2,3,4,5,6,7,8])
sharad1 = sharad.reshape(2, 2, -1)
print(sharad1)

# Flattening the array by converting multidimensional array in 1-D.
import numpy as np
sharad = np.array([[1,2,3], [4,5,6]])
sharad1 = sharad.reshape(-1)
print(sharad1)

# there are alot of functions for changing the shapes pf an array in numpy. like flatten, ravel and also rearranging the element rot90, flip,fliplr, flipud. they all are actually comes under advanced numpy.