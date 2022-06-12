# slicing array - slicing in python means taking elemetns from one given index to another index.
# [start:end], [start:end:step]

# now we will slice an element from 1 to 5 :
import numpy as np
sharad = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sharad[1:5])

# now we will slice from index 4 to the end value
import numpy as np
sharad = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sharad[4:])

# now we will slice the element from the begining to index 4
import numpy as np
sharad = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sharad[:4])

# Negative Slicing - index 3 to end
import numpy as np
sharad = np.array([1, 2, 3, 4, 5, 6, 7])
print(sharad[-3:-1])

# Step: you will use step value to determine the step of the slicing
# return every other value from index 1 to 5
import numpy as np
sharad = np.array([1, 2, 3, 4, 5, 6, 7])
print(sharad[1:5:2])

# now return every other number from the entire array
import numpy as np
sharad = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(sharad[::2])

# slicing 2-D Array: print 7,8,9
import numpy as np
sharad = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(sharad[1,1:4])

# another example
import numpy as np
sharad = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(sharad[0:2, 2])

# another example tough 2-D - print from both, index 1:4
import numpy as np
sharad = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print(sharad[0:2, 1:4])
