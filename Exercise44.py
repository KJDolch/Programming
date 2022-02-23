"""
Exercise 44 - Reading a File
"""
# read in your second file from Exercise 39, the one with the countdown, by using the generator method
# with open("Datei2.txt", "r") as read_file:
#     for line in read_file:
#         print(line)

# calculate the sum of the numbers and print out the result
sum = 0
with open("Datei2.txt", "r") as read_file:
    for line in read_file:
        sum += int(line)
print("Sum is ", sum)
