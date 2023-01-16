"""Given an integer n, return the number of prime numbers that are strictly less than n.
Example 1:

Input: n = 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
Example 2:

Input: n = 0
Output: 0
Example 3:

Input: n = 1
Output: 0"""
def countPrimes(n):
        if n<2:
            return 0
        is_primes=[True]*(n)
        i=2
        while i*i<=n:
            if is_primes[i]:
                for j in range(i*i,n,i):
                    is_primes[j]=False
            i=i+1
        primes=[i for i in range(2,n) if is_primes[i]==True]
        return len(primes)
v=countPrimes(10)
print(v)