# sort() - the numpy ndarray object has a function which is called sort(), and this will sort a specified array.
import numpy as np
sharad = np.array([3,2,0,1])
print(np.sort(sharad)) # this method is like the copy()

# sort the array alphabetically
import numpy as np
sharad = np.array(['banana', 'cherry', 'apple'])
print(np.sort(sharad))

# sort the boolean array:
import numpy as np
sharad = np.array([True, False, True])
print(np.sort(sharad))

# sorting the 2-D array
import numpy as np
sharad = np.array([[3,2,4], [5,0,1]])
print(np.sort(sharad))