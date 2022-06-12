# products: use prod() function.
# here we will find the product of the element of the below array:
import numpy as np
sharad = np.array([1,2,3,4]) # 1*2*3*4 = 24
sharadnew = np.prod(sharad)
print(sharadnew)

# here we will find the product of elemets in 2 different array:
import numpy as np
sharad1 = np.array([1,2,3,4])
sharad2 = np.array([5,6,7,8])
sharadnew = np.prod([sharad1, sharad2]) # 1*2*3*4*5*6*7*8 = 40320
print(sharadnew)

# product over an axis
import numpy as np
sharad1 = np.array([1,2,3,4])
sharad2 = np.array([5,6,7,8])
sharadnew = np.prod([sharad1, sharad2], axis=1) 
print(sharadnew)

# cummulative product:
# example  the partial product of [1,2,3,4] is [1,1*2,1*2*3,1*2*3*4] = [1,2,6,24] represented by cumprod().
import numpy as np
sharad = np.array([5,6,7,8])
sharadnew = np.cumprod(sharad)
print(sharadnew)