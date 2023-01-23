'''Date:20/01/2023 Name:K Prasad Achari'''

'''You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. 
Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, 
which means: swap s1[i] and s2[j].

Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.'''

from math import ceil
def minimumSwap(s1, s2):
    x1 = 0
    y1 = 0
    for i in range(len(s1)):
        if s1[i] != s2[i] and s1[i] == "x":
            x1 += 1
        if s1[i] != s2[i] and s1[i] == "y":
            y1 += 1
    if (x1 + y1) % 2 != 0:
        return -1        
    return ceil(x1/2)+ceil(y1/2)

s1=input()
s2=input()
print(minimumSwap(s1, s2))

'''Input: s1 = "xx", s2 = "yy"
Output: 1'''

'''Input: s1 = "xy", s2 = "yx"
Output: 2'''

'''Input: s1 = "xx", s2 = "xy"
Output: -1'''

