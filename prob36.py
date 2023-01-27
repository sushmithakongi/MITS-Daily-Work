"""find all possible permutations of a given string"""

from itertools import permutations
s=input()
perms = [''.join(p) for p in permutations(s)]
print(perms, end=" ")