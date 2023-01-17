N=int(input())
arr=[]
for i in range(N):  
    s = list(map(int, input().split()))  
    arr.append(s)
x=int(input())
for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == x:
            i_ind=i
            j_ind=j
s=i_ind+j_ind
z=arr[s][j_ind]
res = sum(int(digit) for digit in str(z))
print(res)
