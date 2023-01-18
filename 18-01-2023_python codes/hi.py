#print all k length combinations using itertools
import itertools
a=list(map(int,input().split()))
b=int(input())
print(list(itertools.combinations(a,b)))
