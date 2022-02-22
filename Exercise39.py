"""
Exercise 39 - Pandas DataFrames
"""
# write a program that creates a DataFrame consisting of at least 4 rows and 6 columns.
# The DataFrame should contain random numbers generated via NumPy
# Let the program create 6 new DataFrames by sorting the original DataFrame alongside the columns (df.sort_values())
# let the program print description of the original DataFrame
# What do these numbers mean?

import random
import numpy as np
import pandas as pd

dataframe1 = pd.DataFrame(
    np.random.randn(4, 6),
    index=["Test1", "Test2", "Test3", "Test4"],
    columns=list("ABCDEF"),
)
print(dataframe1)

dataframe2 = dataframe1.sort_values("A")
dataframe3 = dataframe1.sort_values("B")
dataframe4 = dataframe1.sort_values("C")
dataframe5 = dataframe1.sort_values("D")
dataframe6 = dataframe1.sort_values("E")
dataframe7 = dataframe1.sort_values("F")

print(dataframe2)
print(dataframe3)
print(dataframe4)
print(dataframe5)
print(dataframe6)
print(dataframe7)

print(dataframe1.describe())
# the numbers mean: count: how many rows
# mean: what is the mean of this column
# std: standard error
# min/max: the minimum/maximum value
# 25%/ 50%/ 75%: the interquartile ranges
