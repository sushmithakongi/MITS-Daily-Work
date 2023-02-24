"""Problem Statement
Print Internal Varsity Number Square Pattern
In this Python Program, we will be discussing about how to write a program to print Internal Varsity Number Square Pattern. 
In this pattern, there are n*n rows and columns are present.First, We will check if i == 0 or j == 0 or j == cols-1 or i == rows – 1, 
this condition is satisfied, then we will print the border with number “3”. Otherwise, Sequence of a number staring from 1.So, User have to 
enter a single value, that will be determine as a number of rows and columns of the pattern. With the help of “for loop”, we will print the 
Internal Varsity Number Square Pattern."""
rows = int(input("Enter the Number of rows: "))
cols = int(input("Enter the Number of cols: "))

for i in range(0, rows):
    for j in range(0, cols):
        if i == 0 or j == 0 or j == cols-1 or i == rows - 1:
            print("3", end="")
        else:
            print(i, end="")
    print()
