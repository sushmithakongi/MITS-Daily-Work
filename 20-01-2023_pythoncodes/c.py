# This tool returns successive  length k combinations of elements in an iterable.
# If  is not specified or is None, then  defaults to the length of the iterable, 
# and all possible full length permutations are generated.
# combinations are printed in a lexicographic sorted order. So, if the input iterable 
# is sorted, the permutation tuples will be produced in a sorted order.
from itertools import *
a,b=input().split()
l=list(combinations(a,int(b)))
l.sort()
for i in l:
    print(''.join(i))