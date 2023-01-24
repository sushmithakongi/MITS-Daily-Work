"""Merging two sorted list
We have two sorted lists, and we want to write a function to merge the two lists into one sorted list:
a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]"""
def mergesort(a,b):
    k=[]
    k=sorted(a)+sorted(b)
    return sorted(k)
a = [3, 4, 6, 10, 11, 18]
b = [1, 5, 7, 12, 13, 19, 21]
print(mergesort(a,b))