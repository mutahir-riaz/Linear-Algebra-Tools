## take the vector 
## take b1 && b2 
## assign b1 to v[0]
## assign b2 to v[1]
## finding a and b 
import numpy as np
from fractions import Fraction

# Define the vector v and the basis vectors b1 and b2
v = np.array([10, -5])
b1 = np.array([3, 4])
b2 = np.array([4, -3])

# Set up the matrix of basis vectors
B = np.column_stack((b1, b2))
# Solve for the coordinates (a, b)
coordinates = np.linalg.solve(B, v)

# Print the results
a, b = coordinates
a =  Fraction(a).limit_denominator()
b =  Fraction(b).limit_denominator()

print(f"The coordinates of the vector v in the basis defined by b1 and b2 are: a = {a}, b = {b}")
