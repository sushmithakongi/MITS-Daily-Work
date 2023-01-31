n,m=[int(x) for x in input().split()]
inp=[]
for i in range(m):
    inp.append([int(x) for x in input().split()])
    
fam=[]
l=0
minl=n+1
s=set()
for x,y in inp:
    s.add(x)
    s.add(y)
    flag=1
    for i in range(l):
        if x in fam[i] or y in fam[i]:
            fam[i].add(x)
            fam[i].add(y)
            flag=0
    if flag==1:
        fam.append(set())
        fam[l].add(x)
        fam[l].add(y)
        l=l+1
c=0
for i in range(1,n+1):
    if i not in s:
        c+=1
for i in fam:
    minl=min(len(i),minl)
if c!=0:
    minl=min(minl,c)
print(minl)
