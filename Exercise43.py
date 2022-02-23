"""
Exercise 43 - Writing Files
"""
# write a program that creates two different files

# the first file should be opened normally and two lines should be written in it
File = open("Datei1.txt", "w")
File.write("Hello\n")
File.write("This is the second line.\n")
File.close()

# afterwards close the file, open it again and add another three lines of text to the file
File = open("Datei1.txt", "a")
File.write("And one more line\n")
File.write("And still with no information.\n")
File.write("So I will stopp.\n Good Bye\n")

# the second file should be generated by using "with" and a loop to write a countdown from 10 to 0
with open("Datei2.txt", "w") as File_with:
    for i in reversed(range(11)):
        File_with.write(str(i) + "\n")

# each number should be in a seperate line
