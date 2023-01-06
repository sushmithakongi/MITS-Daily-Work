"""Find all triplets with zero sum
Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.
Examples:
Input: arr[] = {0, -1, 2, -3, 1}
Output: (0-11), (2-31)
Explanation: The triplets with zero sum
are 0 + −1 + 1 = 0 and 2 + −3 +1 = 0 """
arr=list(map(int,input().split()))
n=len(arr)
found = False
for i in range(0, n-2): 
    for j in range(i+1, n-1): 
        for k in range(j+1, n):
            if (arr[i] + arr[j]+ arr[k]==0):
                print (arr[i],arr[j],arr[k])
                found=True
if (found == False):
    print(" not exist ")
