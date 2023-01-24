'''Given a list of numbers, write a Python program to count positive and negative numbers in a List. 

Example:

Input: list1 = [2, -7, 5, -64, -14]
Output: pos = 2, neg = 3

Input: list2 = [-12, 14, 95, 3]
Output: pos = 3, neg = 1'''

list1 = [10, -21, 4, -45, 66, -93, 1]
 
pos, neg = 0, 0
 
for num in list1:
 
    if num >= 0:
        pos += 1
 
    else:
        neg += 1
 
print("Positive numbers: ", pos)
print("Negative numbers: ", neg)