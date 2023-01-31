
def isIsomorphic(s,t):
    ds={}
    dt={}
    l=len(s)
    p1=1
    p2=1
    ns=0
    nt=0
    for i in range(l):
        if s[i] not in ds:
            ds[s[i]]=p1
            p1+=1
        if t[i] not in dt:
            dt[t[i]]=p2
            p2+=1
        ns=ns*10+ds[s[i]]
        nt=nt*10+dt[t[i]]
    return ns==nt
print(isIsomorphic("egg","app"))