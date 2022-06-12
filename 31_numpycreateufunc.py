# to create your own ufunc, you have to define a function, like you do in normal function in python, then you add it to the numpy function with frompyfunc() method.
# arguments of frompyfunc(): function, inputs, outputs

# Create your own ufunc for addition:
import numpy as np
def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1,2,3,4], [5,6,7,8]))

# checking if this function in ufunc or not:
import numpy as np
print(type(np.add))

# concatenate()
import numpy as np
print(type(np.concatenate))

# what if ufunc does not exist: (please comment it while running the codes) 
import numpy as np
print(type(np.sjafdfdf))

# use an if statement to check if the functionis  a ufunc or not.
import numpy as np
if type(np.add) == np.ufunc:
    print('yes, this function is ufunc')
else:
    print('this function is not aan ufunc')