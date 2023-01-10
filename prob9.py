"""Given a string str, find the length of the longest substring without repeating characters. """
import math
def substr(str):
    test = ""
    maxLength = -1
    if (len(str) == 0):
        return 0
    elif(len(str) == 1):
        return 1
    for c in list(str):
        current = "".join(c)
        if (current in test):
            test = test[test.index(current) + 1:]
        test = test + "".join(c)
        maxLength = max(len(test), maxLength)
    return maxLength
str=input()
print(substr(str))