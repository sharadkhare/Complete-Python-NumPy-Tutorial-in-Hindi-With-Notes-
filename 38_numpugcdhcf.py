# finding GCD(Gretest common denominator), also known as HCF(Highest Common Factor)

# here wew will find the HCF of the below 2 numbers:
import numpy as np
sharad1 = 6
sharad2 = 9
sharadnew = np.gcd(sharad1, sharad2)
print(sharadnew) # answer will be 3 because that is the highest number  and both umber can be divided by (6/3=2 and 9/3=3)

# finding the GCD in an array
# the reduce() method will use the ufunc, in this case the gcd() function on each elemtn and it will reduce the array by 1 dimension.
import numpy as np
sharad = np.array([20,8,32,16,36])
sharadnew = np.gcd.reduce(sharad)
print(sharadnew)
# it will return 4 because 4 is the highest number of all values that can be divided in between array.