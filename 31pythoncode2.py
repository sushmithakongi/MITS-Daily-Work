# Odd Frequency Characters
# Using list comprehension and defaultdict()
from collections import defaultdict
 
#function
def hlp(test):
    cntr = defaultdict(int)
    for ele in test:
        cntr[ele] += 1
    return [val for val, chr in cntr.items() if chr % 2 != 0]
 
# initializing string
test = "Every cloud has a silver lining"
 
# printing original string
print("The original string is : " + str(test))
 
# Odd Frequency Characters
# Using list comprehension + defaultdict()
res = hlp(test)
 
# printing result
print("The Odd Frequency Characters are :" + str(res))
