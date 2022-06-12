# Getting some elements out of an existing array and creating a new array is called filtering.
# A boolean index list is a list ofboolean corresponding to indexes in the array. (True and False)
# create an array from the element on index 0 to 2:
import numpy as np
sharad = np.array([41,42,43,44])
sharad1 = [True, False, True, False]
finalsharad = sharad[sharad1]
print(finalsharad)

# now we will create a filter array
# that will return only values higher than 42.
import numpy as np
sharad = np.array([41,42,43,44])
emptysharad = []
for element in sharad:
    if element > 42:
        emptysharad.append(True)
    else:
        emptysharad.append(False)
sharadnew = sharad[emptysharad]
print(emptysharad)
print(sharadnew)

# Create a filter array that will return only even elements from the original array.
import numpy as np
sharad = np.array([1,2,3,4,5,6,7])
sharadempty = []
for i in sharad:
    if i%2 == 0:
        sharadempty.append(True)
    else:
        sharadempty.append(False)
sharadnew = sharad[sharadempty]
print(sharadempty)
print(sharadnew)

# Yes, you can also create filter directly from array
# that will return only values higher than 42.
import numpy as np
sharad = np.array([41,42,43,44])
sharadempty = sharad > 42
sharadnew = sharad[sharadempty]
print(sharadempty)
print(sharadnew)

# Yes, you can also create filter directly from array
# Create a filter array that will return only even elements from the original array.
import numpy as np
sharad = np.array([1,2,3,4,5,6,7])
sharadempty = sharad % 2 == 0
sharadnew = sharad[sharadempty]
print(sharadempty)
print(sharadnew)