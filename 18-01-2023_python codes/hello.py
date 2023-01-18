#print all k length permutations using itertools
import itertools
a=list(map(int,input().split()))
k=int(input())
for i in list(itertools.permutations(a,k)):
    print(i)
