# difference: use diff() function for finding the difference
# example: [1,2,3,4],  the deiscreate difference of this would be [2-1, 3-2, 4-3] = [1,1,1] by using diff()
import numpy as np
sharad = np.array([10,15,25,5]) # [5, 10, -20] because 15-10=5, 25-15=10 and 5-25=-20
sharadnew = np.diff(sharad)
print(sharadnew)

