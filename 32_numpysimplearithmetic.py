# arithemtic operators: +, -, / , *
# by using ufunc additional arguments like, where, dtype and out.
# here now we will use add()
import numpy as np
sharad1 = np.array([10,11,12,13,14,15])
sharad2 = np.array([20,21,22,23,24,25])
sharadnew = np.add(sharad1, sharad2)
print(sharadnew)

#  example of substracting the value
import numpy as np
sharad1 = np.array([10,11,12,13,14,15])
sharad2 = np.array([20,21,22,23,24,25])
sharadnew = np.subtract(sharad1, sharad2)
print(sharadnew)

# example of multipication
import numpy as np
sharad1 = np.array([10,11,12,13,14,15])
sharad2 = np.array([20,21,22,23,24,25])
sharadnew = np.multiply(sharad1, sharad2)
print(sharadnew)

# example of divide()
import numpy as np
sharad1 = np.array([10,11,12,13,14,15])
sharad2 = np.array([20,21,22,23,24,25])
sharadnew = np.divide(sharad1, sharad2)
print(sharadnew)

# power() function raises the value from the 1st array to the power of the values of the 2nd array and return the results in a new array.

import numpy as np
sharad1 = np.array([10,20,30,40,50,60])
sharad2 = np.array([3,5,6,8,2,33])
sharadnew = np.power(sharad1, sharad2)
print(sharadnew)

# reminder- mod() and reminder() fucntions return the reminder of the 1st array corrosponding to the 2nd array, and result in the new array.
import numpy as np
sharad1 = np.array([10,20,30,40,50,60])
sharad2 = np.array([3,7,9,8,2,33])
sharadnew = np.mod(sharad1, sharad2)
print(sharadnew)

# by using reminder()
import numpy as np
sharad1 = np.array([10,20,30,40,50,60])
sharad2 = np.array([3,7,9,8,2,33])
sharadnew = np.remainder(sharad1, sharad2)
print(sharadnew)

# quotient and mod(reminder)
# the divmod() function return both the quotient and mod.
import numpy as np
sharad1 = np.array([10,20,30,40,50,60])
sharad2 = np.array([3,7,9,8,2,33])
sharadnew = np.divmod(sharad1, sharad2)
print(sharadnew)

# absolute() and abs()- do the same operation but here we should use absolute() to avoid confusion with python inbuilt function math.abs().
import numpy as np
sharad = np.array([-1,-2,-3,-4,-5])
sharadnew = np.absolute(sharad)
print(sharadnew) 
