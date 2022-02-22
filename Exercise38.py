"""
Exercise 38 - NumPy arrays
"""
# wirte a simple python program that generates the following arrays
import numpy as np

# an array consisting of 25 zeros
Array1 = np.zeros(25)

# an array consisting of 8 ones
Array2 = np.ones(8)

# an array consisting of numbers from 0 to 24 in order
Array3 = np.arange(25)

# an array consisting of 9 entries of your choice
Array4 = np.array([7, 5, 3, 9, 6, 2, 8, 5, 1])

# a two-dimensional array TD consisting of 6 rows of arrays with 5 entries
Array5 = np.ones((6, 5))

# a transposed version of the two-dimensional array # TD
Array6 = Array5.transpose()

print("Array [1]", Array1)
print("Array [2]", Array2)
print("Array [3]", Array3)
print("Array [4]", Array4)
print("Array [5]", Array5)
print("Array [6]", Array6)
list = [Array1, Array2, Array3, Array4, Array5, Array6]
# write furthermore an algorithm to print out the sum, maximum value, minimum value and shape of all created arrays

for i in range(len(list)):
    print("Array", [i + 1])
    Sum = list[i].sum()
    print("The sum of the array is", Sum)

    Max = list[i].max()
    print("The maximum of the array is", Max)

    Min = list[i].min()
    print("The minimum of the array is", Min)

    Shape = list[i].shape
    print("The shape of the array is", Shape)
    print("")
