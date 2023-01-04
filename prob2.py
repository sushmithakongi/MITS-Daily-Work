"""Given an integer array nums, return the length of the longest strictly increasing 
subsequence
.

 

Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4."""
def lis(arr):
    n = len(arr)
    lis = [1]*n
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j]+1
    maximum = 0
    for i in range(n):
        maximum = max(maximum, lis[i])
    return maximum
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print ("Length of lis is", lis(arr))