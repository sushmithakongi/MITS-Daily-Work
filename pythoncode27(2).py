'''Date : 27/01/2023 Name : K Prasad Achari'''

'''Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, 
she eats all of them instead and will not eat any more bananas during this hour.
Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
Return the minimum integer k such that she can eat all the bananas within h hours.'''

from math import ceil
def minEatingSpeed(piles, h):
    def p(m):
        s=0
        for i in piles:
            s+=ceil(i/m)
        return s<=h
    l=1
    r=max(piles)
    while l<=r:
        m=(l+r)//2
        if p(m):
            ans=m
            r=m-1
        else:
            l=m+1
    return ans

piles=list(map(int,input().split(",")))
h=int(input())
print(minEatingSpeed(piles, h))

'''Input: 
piles = [3,6,7,11], h = 8
Output: 4
'''
'''Input:
piles = [30,11,23,4,20], h = 5
Output: 30'''