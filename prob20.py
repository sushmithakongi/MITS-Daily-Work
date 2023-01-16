"""here are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:
In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.
Return the maximum number of coins that you can have.
Example 1:

Input: piles = [2,4,1,2,7,8]
Output: 9"""
def maxCoins(piles):
        my_coins = 0
        piles.sort()
        for i in range(len(piles)//3):
            my_coins += piles[-2 - 2*i]
        
        return my_coins
piles=list(map(int,input().split()))
print(maxCoins(piles))