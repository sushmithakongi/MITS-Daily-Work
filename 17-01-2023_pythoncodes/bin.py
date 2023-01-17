# Flip String to Monotone Increasing
# A binary string is monotone increasing if it consists of some number of 0's 
# (possibly none), followed by some number of 1's (also possibly none).
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 
# or from 1 to 0.
# Return the minimum number of flips to make s monotone increasing.
# Input: s = "00110"
# Output: 1
# Explanation: We flip the last digit to get 00111.
s=input()
o, a = 0, 0                    
for n in s:                       
    if n =='1': o += 1         
    elif o:                     
        o -= 1                  
        a += 1                    
print(a)