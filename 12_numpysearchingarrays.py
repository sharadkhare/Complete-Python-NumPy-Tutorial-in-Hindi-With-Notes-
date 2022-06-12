# searching array - you can search an array for a certain value and return the indexes that get the match. by using where()
import numpy as np
sharad = np.array([1,2,3,4,5,4,4])
sharadnew = np.where(sharad == 4)
print(sharadnew)

# now we will find the indexes where the values are even:
import numpy as np
sharad = np.array([1,2,3,4,5,6,7,8])
sharad1 = np.where(sharad%2 == 0)
print(sharad1)

# now we will find the indexes where the values are odd:
import numpy as np
sharad = np.array([1,2,3,4,5,6,7,8])
sharad1 = np.where(sharad%2 == 1)
print(sharad1)

# Searchsorted() - perform binary search in array.
# we will now find the index where the value 7 should be insterted.
import numpy as np
sharad = np.array([6,7,8,9])
sharad1 = np.searchsorted(sharad, 7)
print(sharad1)

# now we will search fron right side
import numpy as np
sharad = np.array([6,7,8,9])
sharad1 = np.searchsorted(sharad, 7, side='right')
print(sharad1)

# how to search multiple values:
import numpy as np
sharad = np.array([1,3,5,7])
sharad1 = np.searchsorted(sharad, [2,4,6])
print(sharad1)