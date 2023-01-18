'''Power of Two
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

Constraints:

-231 <= n <= 231 - 1'''
def isPowerOfTwo(n):
    
    # If n <= 0 that means its a negative hence not a power of 2...
    if n <= 0:
        return False
    if n == 1:
        return True
    # Keep dividing the number by ‘2’ until it is not divisible by ‘2’ anymore.
    while (n % 2 == 0):
        n /= 2
    # If n is equal to 1, The integer is a power of two otherwise false...
    return n == 1
n=int(input("enter a value"))
print(isPowerOfTwo(n))