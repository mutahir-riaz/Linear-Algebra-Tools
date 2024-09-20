import re  # Import regular expressions module for parsing equations
import numpy as np  # Import NumPy for numerical operations, especially with matrices
from fractions import Fraction  # Import Fraction to handle rational numbers

def parse_equation(equation):
    # Regex to capture coefficients of the variables and the constant
    pattern = r"([-+]?\d*)\s*([a-zA-Z])\s*([-+]?\d*)\s*([a-zA-Z])\s*=\s*([-+]?\d+)"
    # Match the input equation against the regex pattern
    match = re.match(pattern, equation.replace(" ", ""))

    if match:
        # Extract components of the equation
        a = match.group(1)  # Coefficient of the first variable
        b = match.group(3)  # Coefficient of the second variable
        
        # Handle cases like '+x' or '-y' where there's no explicit number before the variable
        a = int(a) if a and a not in ['+', '-'] else (1 if a == '' or a == '+' else -1)
        b = int(b) if b and b not in ['+', '-'] else (1 if b == '' or b == '+' else -1)

        x = match.group(2)  # First variable name
        y = match.group(4)  # Second variable name
        c = int(match.group(5))  # Constant on the right side
        
        return [a, b], [x, y], c  # Return coefficients, variables, and constant
    else:
        raise ValueError("Invalid equation format.")  # Raise an error for invalid format

def equations_to_matrix(eq1, eq2):
    # Parse both equations to extract coefficients and constants
    coeffs1, variables1, const1 = parse_equation(eq1)
    coeffs2, variables2, const2 = parse_equation(eq2)
    
    # Assuming both equations have the same variables, get a unique set of variables
    variables = list(set(variables1 + variables2))
    
    # Create the coefficient matrix (2x2) from the coefficients
    matrix = np.array([coeffs1, coeffs2])
    
    # Create the solution vector (the right-hand side constants)
    solution_vector = np.array([const1, const2])
    
    return matrix, variables, solution_vector  # Return matrix, variables, and solution vector

# Example usage
eq1 = input("Enter the first equation : ")  # Prompt user for the first equation
eq2 = input("Enter the second equation : ")  # Prompt user for the second equation

# Convert equations to matrix form and extract solution vector
matrix, variables, solution_vector = equations_to_matrix(eq1, eq2)
# Solve the linear equations using NumPy's linear algebra solver
solution = np.linalg.solve(matrix, solution_vector)
[a, b] = solution  # Unpack the solution into variables a and b
# Convert solutions to fractions for better representation
a = Fraction(a).limit_denominator()
b = Fraction(b).limit_denominator()

# Print the results
print("Coefficient Matrix:\n", matrix)  # Output the coefficient matrix
print("Variables:", variables)  # Output the variable names
print("Solution Vector:", solution_vector)  # Output the solution vector
print(f"Solution for {eq1} and {eq2} a = {a} b = {b}")  # Output the solutions
