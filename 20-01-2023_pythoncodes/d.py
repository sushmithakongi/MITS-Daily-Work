# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).
l=list(map(int,input().split()))
m=list(map(int,input().split()))
l.sort()
m.sort()
k=[]
for i in l:
    for j in m:
        k.append((i,j))
print(' '.join(list(map(str,k))))
