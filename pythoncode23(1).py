'''Date:23/01/2023 Name:K Prasad Achari'''

'''Given a list of non negative integers, arrange them in such a manner that they form the largest number possible.
The result is going to be very large, hence return the result in the form of a string.'''

def printLargest(arr):
    if len(arr)==1:
        return str(arr[0])
    for i in range(len(arr)):
        arr[i]=str(arr[i])
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[j]+arr[i]>arr[i]+arr[j]:
                arr[i],arr[j]=arr[j],arr[i]
    result=''.join(arr)
    if(result=='0'*len(result)):
        return '0'
    else:
        return result

arr=list(map(int,input().split(",")))
print(printLargest(arr))

'''Input: 
arr = [3, 30, 34, 5, 9]
Output: 9534330'''

'''Input: 
arr = [54, 546, 548, 60]
Output: 6054854654'''
