# This tool returns the  length subsequences of elements from the input iterable.
# Combinations are emitted in lexicographic sorted order. So, if the input iterable is sorted, 
# the combination tuples will be produced in sorted order.
from itertools  import *
a,b=input().split()
for i in range(1,int(b)+1):
    l=list(combinations(a,i))
    g=[]
    for j in l:
        i=list(j)
        i.sort()
        g.append(i)
    g.sort()
    for i in g:
        print(''.join(i))
    