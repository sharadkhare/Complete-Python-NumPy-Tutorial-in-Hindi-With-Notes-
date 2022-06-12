# Trigonometric function: numpy provides the ufuncs line sin(), cos() and tan() that takes values in radians and produce the corresponding sin, cos and tan values.
# here now we will find the sin value of pi/2
import numpy as np
sharad = np.sin(np.pi/2)
print(sharad)

# we will now find the sin values of an array
import numpy as np
sharad = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
sharadnew = np.sin(sharad)
print(sharadnew)

# Convert Degree into radians: by default all of the trigonometric functions tales radians as parameter.
# note: radians values are pi/180* degree value.
# here we will convert all the array values to radians:
import numpy as np
sharad = np.array([90, 180, 270,360])
sharadnew = np.deg2rad(sharad)
print(sharadnew)

# here we will convert radians into degree.
import numpy as np
sharad = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
sharadnew = np.rad2deg(sharad)
print(sharadnew)

# here we can also find angles : arcsin(), arccos() and arctan() that takes values in radians and produce the corresponding sin, cos and tan values.

# we will now find the angle of 1.0
import numpy as np
sharad = np.arcsin(1.0)
print(sharad)

# angles of each values in an array:
import numpy as np
sharad = np.array([1, -1, 0.1])
sharadnew = np.arcsin(sharad)
print(sharadnew)

# here we can also find the hypotenous using the pythagoras theorem in numpy
# hypot() function that takes values in radians and produce the corresponding sin, cos and tan values.

# here we will find the hypot for 3 base and 4 perpendicular.
import numpy as np
base = 3
perp = 4
sharad = np.hypot(base, perp)
print(sharad)

