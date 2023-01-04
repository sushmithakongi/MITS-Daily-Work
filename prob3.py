#prob3.py
#find the missing number in a given series of numbers
def MissingNumber(array,n):
        l=sum(array)
        o=(n*(n+1))/2
        return l-o
n=int(input())
array=list(map(int,input().split()))
s=MissingNumber(array,n)
print(int(s))