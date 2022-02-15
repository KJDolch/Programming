"""
Exercise 15 - New matrices
"""

print("Quadratic matrix")
matrix1 = [[0, 1], [0, 1]]
print(matrix1)

print("More colums than rows")
matrix2 = [[0, 1, 2], [0, 1, 2]]
print(matrix2)
matrix3 = [list(range(3))] * 2

print("more rows than columns")
matrix4 = [[0, 1], [0, 1], [0, 1]]
print(matrix4)
matrix5 = [list(range(2))] * 3

dimension6 = int(input("How do you want the diemension of matrix6: "))

matrix6 = [list(range(2))] * dimension6
print(matrix6)
