"""
Exercise 34 - Working with os
"""
# create a directory structure by using os
import os

# os.system("clear")
# create one parent directory with at least five child directories
os.makedirs("Parent", exist_ok=True)
os.chdir("Parent")
os.makedirs("Child1", exist_ok=True)
os.chdir("Child1")
os.system("touch child1.txt")

os.chdir("..")
os.makedirs("Child2", exist_ok=True)
os.chdir("Child2")
os.system("touch child2.txt")

os.chdir("..")
os.makedirs("Child3", exist_ok=True)
os.chdir("Child3")
os.system("touch child3.txt")

os.chdir("..")
os.makedirs("Child4", exist_ok=True)
os.chdir("Child4")
os.system("touch child4.txt")

os.chdir("..")
os.makedirs("Child5", exist_ok=True)
os.chdir("Child5")
os.system("touch child5.txt")

# oder mit loop:

os.mkdir("Exercise34")
os.chdir("Exercise34")

Dirs = ["Dir1", "Dir2", "Dir3", "Dir4", "Dir5"]

for Dir in Dirs:
    os.mkdir(Dir)
    os.chdir(Dir)
    os.system("touch " + Dir + ".txt")
    os.chdir("..")
