'''Given a String, perform uppercase of later part of string

nput : test_str = ‘apples’ 

Output : appLES 

Explanation : Latter half of string is uppercased.'''

test_str = 'apples'
 
print("The original string : " + str(test_str))
 
hlf= len(test_str) // 2
 
res = ''
for i in range(len(test_str)):
 
    if i >= hlf:
        res += test_str[i].upper()
    else:
        res += test_str[i]
 
print("The resultant string : " + str(res))