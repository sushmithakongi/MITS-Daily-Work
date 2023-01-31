"""A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. They are now trying out various combinations of company names and logos based on this condition. Given a string , which is the company name in lowercase letters, your task is to find the top three most common characters in the string.
Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
Sample Input 
aabbbccde
Sample Output 
b 3
a 2
c 2
"""
from collections import Counter
s = sorted(input())
for i in range(3):
    print(*Counter(s).most_common()[i])