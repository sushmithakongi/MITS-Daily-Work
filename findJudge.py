def findJudge(n,trust):
    d={i:set() for i in range(1,n+1)}
    nrmlp=set()
    for i,j in trust:
        d[j].add(i)
        nrmlp.add(i)
    for i in d:
        if len(d[i])==n-1 and i not in nrmlp:
            return i
    return -1
print(findJudge(2,[[1,2]]))
