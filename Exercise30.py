"""
Exercise 30 - Functions with nested loops
"""

# function for max value of the matrix:
def MaxV(matrix):
    maximum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > maximum:
                maximum = matrix[i][j]
    return maximum


import random

testmatrix = [
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
]
print(testmatrix)

MaxValue = MaxV(testmatrix)
print("The maximal value of the matrix is ", MaxValue)

# function for the sum of the matrix
def SumUp(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
    return sum


Summe = SumUp(testmatrix)
print("The sum of the matrix is ", Summe)

# function for the multiplication of the components of two matrices in a third resulting matrix
def MultiMatrices(matrix1, matrix2):
    resultmatrix = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            resultmatrix[i][j] = matrix1[i][j] * matrix2[i][j]
    return resultmatrix


testmatrix1 = [[1, 2], [1, 2]]
testmatrix2 = [[3, 4], [3, 4]]

Multi = MultiMatrices(testmatrix1, testmatrix2)
print("The resulting muliplicates matrix is: ", Multi)

# oder wenn unbekannte Testmatices
testmatrix1 = [
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
]
print("Our random matrix1 looks like this:\n", testmatrix1)
testmatrix2 = [
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
]
print("Our random matrix2 looks like this:\n", testmatrix2)
print("")


def MatrixMulti(InputMatrix1, InputMatrix2):
    resultmatrix = []
    for i in range(len(InputMatrix1)):
        resultmatrix.append([])
        for j in range(len(InputMatrix1[i])):
            product = testmatrix1[i][j] * testmatrix2[i][j]
            resultmatrix[i].append(product)
    return resultmatrix


MultiMatrix = MatrixMulti(testmatrix1, testmatrix2)
print("The resultmatrix looks like this:\n", MultiMatrix)
