# import a pakage named numpy
import numpy as npy

# Ask user for number of equations i.e. rows
eq = int(input("Enter the number of equations: "))

# Ask user for number of variables i.e. columns
var = int(input("Enter the number of variables: "))

'''
Initialize matrix using numpy
And, done var+1 to add a column for constant & for making an augmented matrix
'''
matrix = npy.zeros((eq, var+1))

# Taking input from the user for the matrix
for i in range(eq):
    print(f"Enter the coefficient for equation {i+1}: ")
    for j in range(var):
        matrix[i][j] = float(input(f" Enter the coefficient for variable {j+1}: "))
    matrix[i][var] = float(input(f" Enter the constant for equation {i+1}: "))

print("Matrix formed: ")
print(matrix)

# Performing row operations using conditional operators

for i in range(eq):
    max_row = i
    for j in range(i+1, eq):
        if abs(matrix[j][i]) > abs(matrix[max_row][i]):
            max_row = j
    matrix[[i, max_row]] = matrix[[max_row, i]]
    matrix[i] /= matrix[i][i]

    for j in range(eq):
        if i != j:
            matrix[j] -= matrix[j][i] * matrix[i]

# Printing the final output i.e. Reduced Row Echelon form of Matrix
print("Matrix in Reduced Row Echelon Form:")
print(matrix)

# Can reduce matrix who is having unique solution only.
