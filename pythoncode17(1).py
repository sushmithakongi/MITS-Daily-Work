'''Dtae:17/01/2023 Name: K Prasad Achari'''
'''Given an array A of N elements. Find the majority element in the array.
 A majority element in an array A of size N is an element that appears more than N/2 times in the array.'''

def majorityElement(n, a):
    dic={}
    for i in a:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    
    for key,value in dic.items():
        if value > (n//2):
            return key
        else:
            return -1

n=int(input())
a=list(map(int,input().split(",")))
print(majorityElement(n, a))

'''Input:n = 3 a = [1,2,3] 
Output:-1'''
'''Input:
a = 5 
a = [3,1,3,3,2] 
Output:3'''
