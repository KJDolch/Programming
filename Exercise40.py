"""
Exercise 40 - argparse
"""
# write a program using the module argparse that takes some strings as input and concatenates these strings in the order of input to one new string
# add at least three other arguments besides the strings that modify the program in different ways
# the program could add spaces or could reverse the order of the input strings for example

import argparse

parser = argparse.ArgumentParser(description="Process some strings.")
# positional argument
parser.add_argument(
    "strings", metavar="S", type=str, nargs="+", help="the strings to concatenate"
)
# opotional arguments
parser.add_argument(
    "-s", "--space", action="store_true", help="add space to the string"
)

parser.add_argument(
    "-r", "--reverse", action="store_true", help="reverse the string order"
)

parser.add_argument("-so", "--sort", action="store_true", help="sorts the strings")

args = parser.parse_args()
if args.reverse:
    args.strings = reversed(args.strings)
    print(args.strings)

if args.sort:
    args.strings = sorted(args.strings)
    print(args.strings)

Bigword = ""
for word in args.strings:
    Bigword += word
    if args.space:
        Bigword += " "

print(Bigword)
