N=int(input())
arr=[]
for i in range(N):  
    s = list(map(int, input().split()))  
    arr.append(s) 
x,y=input().split(" ")
sumd=0
for i in range(0, N):
        sumd += arr[i][i]
l=arr[int(x)][int(y)]
s=str(l)
if(len(s)==1):
    res=int(sumd/l)
    print(res)
else:
    l1= (l- 1) % 9 + 1 if l > 0 else 0
    res=int(sumd/l1)
    print(res)
    
                         
