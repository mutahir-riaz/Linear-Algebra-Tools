import numpy as np
from fractions import Fraction

# Define the vector v that you want to express in terms of the basis vectors b1 and b2
v = np.array([10, -5])

# Define the basis vectors b1 and b2
b1 = np.array([3, 4])
b2 = np.array([4, -3])

# Stack the basis vectors b1 and b2 into a matrix B as column vectors
# This matrix represents the change of basis from the standard basis to the new basis
B = np.column_stack((b1, b2))

# Use numpy's linear solver to solve the system B * [a, b] = v
# This will give us the coordinates a and b such that v = a * b1 + b * b2
coordinates = np.linalg.solve(B, v)

# Extract the values of a and b from the solution
a, b = coordinates

# Convert a and b into fractions to display exact values
a = Fraction(a).limit_denominator()
b = Fraction(b).limit_denominator()

# Print the coordinates of vector v in terms of the new basis {b1, b2}
print(f"The coordinates of the vector v in the basis defined by b1 and b2 are: a = {a}, b = {b}")
