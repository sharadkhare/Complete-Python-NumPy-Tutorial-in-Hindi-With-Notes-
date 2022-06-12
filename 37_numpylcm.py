# finding LCM(Lowest Common Multiple)
# here we will find the LCM of the 2 numbers:

import numpy as np
sharad1 = 4
sharad2 = 6
sharadnew = np.lcm(sharad1, sharad2)
print(sharadnew)
# the answers of the above is 12 because the LCM of both numbers (4*3=12 and 6*2=12) 

# finding the LCM in array:
import numpy as np
sharad = np.array([3,6,9])
sharadnew = np.lcm.reduce(sharad) # the reduce() method will use the ufunc, in this case the lcm() function on each elemtn and it will reduce the array by 1 dimension.
print(sharadnew)


# here we will find the LCM of all of an array where the array contains all integers from 1 to 10.
import numpy as np
sharad = np.arange(1,11)
sharadnew = np.lcm.reduce(sharad)
print(sharadnew)