#!/usr/bin/python3
for i in range(9):
    for j in range(i + 1, 10):
        print("{:d}".format(i), end="")
        if i == 8 and j == 9:
            print("{:d}".format(j))
        else:
            print("{:d}".format(j), end=", ")
