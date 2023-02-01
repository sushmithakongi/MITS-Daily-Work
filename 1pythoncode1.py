"""Given an integer array of n integers, find sum of bit differences in all pairs that can be formed from array elements. 
Bit difference of a pair (x, y) is count of different bits at same positions in binary representations of x and y. 
For example, bit difference for 2 and 7 is 2. Binary representation of 2 is 010 and 7 is 111
( first and last bits differ in two numbers)"""

def BD(arr, n):
    ans = 0 
    for i in range(0, 32):
        count = 0
        for j in range(0, n):
            if ( (arr[j] & (1 << i)) ):
                count+= 1
        ans += (count * (n - count) * 2);
    return ans
arr = list(map(int,input().split()))
n = len(arr)
print(BD(arr, n))