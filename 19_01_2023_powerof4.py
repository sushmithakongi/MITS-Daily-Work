'''
Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true
 

Constraints:

-231 <= n <= 231 - 1
'''

def isPowerOfFour(n):
    i = 0
    curr = 0
    while curr <= n:
        curr = 4 ** i
        if curr == n:
            return True
        i += 1
    return False
n=161
print(isPowerOfFour(n))