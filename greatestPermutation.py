ls=input().split()
nl=[]

for i in ls:
    n=[d for d in i]
    n.sort(reverse=True)
    n="".join(n)
    n=int(n)
    nl.append(n)
nl.sort(reverse=True)
print(nl[0])
