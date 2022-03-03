"""
Exercise 15 - New matrices
"""
# write a program that creates at least three different matrices with different sizes
# for ths exercise rows stands for the numbers of sublists and columns for the number of entries in the sublists
# one of them should be quadratic
print("Quadratic matrix")  # quadratic means: same number of columns and rows
matrix1 = [[0, 1], [0, 1]]
print(matrix1)
# one should have more columns than rows
print("More colums than rows")
matrix2 = [[0, 1, 2], [0, 1, 2]]
print(matrix2)
matrix3 = [list(range(3))] * 2
# one should have more rows than columns
print("more rows than columns")
matrix4 = [[0, 1], [0, 1], [0, 1]]
print(matrix4)
matrix5 = [list(range(2))] * 3
# let the user input the dimensions of your matrices
dimension6 = int(input("How do you want the diemension of matrix6: "))
dimension7 = int(input("How do you want the diemension of matrix6: "))
matrix6 = [list(range(dimension6))] * dimension7
print(matrix6)
