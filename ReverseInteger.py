
def reverse(x):
    a=str(x)
    neg=False
    l=0
    r=len(a)-1
    s=""
    m=(2**31)-1
    n=-2**31
    if x==0:
        return 0
    if a[0]=="-":
        l=1
        neg=True
    else:
        l=0
    while (r>=0 and a[r]=="0"):
        r-=1
    if neg==True:
        s=a[0]+a[r:l-1:-1]
            #return s
        if not(n<int(s) and int(s)<m):
            return 0
        else:
            return s
    else:
        p=[a[i] for i in range(l,r+1)]
        while (l<=r):
            p[l],p[r]=p[r],p[l]
            l+=1
            r-=1
        k="".join(p)
        if not(n<int(k) and int(k)<m):
            return 0
        else:
            return k
print(reverse(123))