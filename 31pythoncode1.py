# Word location in String
import re
 
# initializing string
test = 'Never blame other people for your problems'
 
# printing original string
print("The original string is : " + test)
 
# initializing word
wrd = 'people'
 
# Using findall() and index()
test = test.split()
res = -1
for idx in test:
    if len(re.findall(wrd, idx)) > 0:
        res = test.index(idx) + 1
 
# printing result
print("The location of word is : " + str(res))