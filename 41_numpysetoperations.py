# what is set? : a set is a collection of unique elements

# for creating the set we use numpy's unique() method to find the unique elements from any array:
# here we will convert the array with repeted elements to a set
import numpy as np
sharad = np.array([1,1,1,2,3,4,5,5,6,7])
sharadnew = np.unique(sharad)
print(sharadnew)

# to find the unique values of 2 1D array, we will use union1d() method
import numpy as np
sharad1 = np.array([1,2,3,4])
sharad2 = np.array([3,4,5,6])
sharadnew = np.union1d(sharad1, sharad2)
print(sharadnew)

# to find the only values tat are present in both array, we will use intersect1d() method.
import numpy as np
sharad1 = np.array([1,2,3,4])
sharad2 = np.array([3,4,5,6])
sharadnew = np.intersect1d(sharad1, sharad2, assume_unique=True)
print(sharadnew)

# to find the only values that are in 1st set and NOT present in the 2nd set: use setfdiff1d()
import numpy as np
sharad1 = np.array([1,2,3,4])
sharad2 = np.array([3,4,5,6])
sharadnew = np.setdiff1d(sharad1, sharad2, assume_unique=True)
print(sharadnew)

# to find the only values that are NOT present in BOTH the sets, use setxor1d() method:
import numpy as np
sharad1 = np.array([1,2,3,4])
sharad2 = np.array([3,4,5,6])
sharadnew = np.setxor1d(sharad1, sharad2, assume_unique=True)
print(sharadnew)






