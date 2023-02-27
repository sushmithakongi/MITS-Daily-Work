#Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m. 
#Task is to check whether a2[] is a subset of a1[] or not.
#Both the arrays can be sorted or unsorted
a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
d = {}
for i in a2 :
    d[i] = d.get(i,0) + 1
for i in a1 :
    if i in d :
        d[i] -= 1
        if d[i] == 0 :
            del d[i]
print('No' if d else 'Yes')