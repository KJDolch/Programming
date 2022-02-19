"""
Exercise 25 - Loop through a matrix
"""
import random

testmatrix = [
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
    list(random.sample(range(10, 100), 5)),
]
print(testmatrix)

# search for the coordinates of maximal value of the matrix
# search for highest number in each list:


maxmatrix = 0
maxi = 0
maxj = 0

for i in range(3):
    for j in range(5):
        if testmatrix[i][j] > maxmatrix:
            maxmatrix = testmatrix[i][j]
            maxi = i
            maxj = j

print("The maximum of", maxmatrix, "is in list", maxi, "at index", maxj)

# sum up all entries of the matrix
print(testmatrix[0])
print(testmatrix[1])
print(testmatrix[2])

sum = 0

for row in testmatrix:
    for elem in row:
        sum += elem
print(sum)

# describe the multiplication of the components of two matrices in a third resulting matrix
matrix1 = [[3, 5, 5], [5, 4, 1]]
matrix2 = [[1, 4, 7], [2, 3, 4]]
result = [[0, 0, 0], [0, 0, 0]]

for i in range(2):
    for j in range(3):
        result[i][j] = matrix1[i][j] * matrix2[i][j]
print("Multiplied Matrix:")
print(result)
