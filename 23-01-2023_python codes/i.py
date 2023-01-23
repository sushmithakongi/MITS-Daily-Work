# 2. Minimum Swaps to Make Strings Equal
# You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. 
# Your task is to make these two strings equal to each other. You can swap any two characters that 
# belong to different strings, which means: swap s1[i] and s2[j].
# Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.
from math import ceil
a=b=0
s1,s2=input(),input()
for i in range(len(s1)):
    if s1[i]!=s2[i]:
        if s1[i]=='x':
            a+=1
        else:
            b+=1
if (a+b)%2==1:print(-1)
else:print(ceil(a/2)+ceil(b/2))
        