"""
Exercise 45 - Copying files
"""
# write a program that takes the name of a file from the user and generates a copy of this file
name = input("What is the name of the file ")


# file = open(name, "w")
# file.close()


# the copy should be generated by writing the contents of the original file into a new file line by line. Use generators to optimize your memory usage for this exercise.

with open(name, "r") as read_file:
    with open("Copy_" + name, "w") as write_file:
        for line in read_file:
            write_file.write(line)
