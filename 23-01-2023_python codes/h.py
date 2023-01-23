# 1. Find the Town Judge
# In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is
# secretly the town judge.
# If the town judge exists, then:The town judge trusts nobody.
# Everybody (except for the town judge) trusts the town judge.
# There is exactly one person that satisfies properties 1 and 2.
# You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts 
# the person labeled bi.
# Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.
n,trust=int(input()),eval(input())
d={i:set() for i in range(1,n+1)}  #here key acts as a town judge and value acts as a trustable persons to key
r=set() #set of not eligible for town judge
t=0
for i,j in trust:
    d[j].add(i)
    r.add(i)
for i,j in d.items():
    if len(j)==n-1 and i not in r:
        print(i)
        t=1
        break
if t==0:print(-1)