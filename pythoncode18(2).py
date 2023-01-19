'''Date:18/01/2023 Name:K Prasad Achari'''
'''Given two arrays X and Y of positive integers, find the number of pairs such that xy > yx 
(raised to power of) where x is an element from X and y is an element from Y.'''

def countPairs(a,b):
    c=0
    for i in a:
        for j in b:
            if ((i**j)>(j**i)):
                c=c+1
    return c

a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(countPairs(a,b))

'''Input: 
a = [2 1 6] 
b = [1 5]
Output: 3'''

'''
Input: 
a = [2 3 4 5]
b = [1 2 3]
Output: 5'''
