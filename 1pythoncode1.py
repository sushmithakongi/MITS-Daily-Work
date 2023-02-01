# Extract string between 2 substrings
# Using loop + index()
 
# initializing 
str1 = "Busy your mind with positive thoughts"
 
print("The original string is : " + str(str1))
 
# initializing substrings
sub1 = "your"
sub2 = "thoughts"
 
# getting index of substrings
idx1 = str1.index(sub1)
idx2 = str1.index(sub2)
 
res = ''
# getting elements in between
for idx in range(idx1 + len(sub1) + 1, idx2):
    res = res + str1[idx]
 
# printing result
print("The extracted string : " + res)