def smallestArray(N,A,K):
    res=[]
    flag=0
    l=0
    for i in range(N-K):
        for j in range(i+1,i+1+K):
            temp=0
            b1=A[i]
            b2=A[j]
            A[i]=A[j]
            A[j]=b1
            for t in range(N):
                temp=temp*10+A[t]
            A[i]=b1
            A[j]=b2
            res.append(temp)
            if flag==0:
                minInd=l
                flag=1
            else:
                if res[minInd]>temp:
                    minInd=l
            l+=1
    ans=[]
    for i in str(res[minInd]):
        ans.append(int(i))
    return ans
print(smallestArray(5,[2,3,3,1,2],3))
