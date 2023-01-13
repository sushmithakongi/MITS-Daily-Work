"""Write a Python program to find the first two elements of a given list whose sum is equal to a given value. Use itertools module to solve the problem"""
import itertools as it
def sum_pairs_list(nums, n):
    for num2, num1 in list(it.combinations(nums[::-1], 2))[::-1]:
        if num2 + num1 == n:
            return [num1, num2]

nums = list(map(int,input().split()))    
n = int(input())
print("Original list:",nums,": Given value:",n)   
print("Sum of pair equal to ",n,"=",sum_pairs_list(nums,n))
