"""
Exercise 60 -
"""
# take your lists from exercise 15 and remove at least two different entries from each of these lists with the help of indices
# let the user choose which entries he wants to have removed after he declares the dimensions of the lists
# run at least one security check (if statement) to see if the given indices are part of the lists (len operator)
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

matrix1[0].remove(matrix1[0][0])
print(matrix1)

matrix3[1].remove(matrix3[1][0])
print(matrix3)

remove1 = int(input("In which sublist do you want to remove: "))
remove2 = int(input("At which index: "))

if remove1 <= dimension7:
    if remove2 <= dimension6:
        matrix6[remove1].remove(matrix6[remove1][remove2])
        print(matrix6)
