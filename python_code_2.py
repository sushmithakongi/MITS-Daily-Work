'''Date:16/01/2023 Name:K Prasad Achari'''
'''A message containing letters from A-Z can be encoded into numbers using the following mapping:
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). 
For example, "11106" can be mapped into:
"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".'''

def numDecodings(str):
    def da(i):
        if i == len(s): 
            return 1
        if s[i] == '0': 
            return 0
            
        return da(i+1) + (da(i+2) if 10 <= int(s[i:i+2]) <= 26 else 0)
        
    return da(0)
s=input()
print(numDecodings(s))

'''Input: s = "226"
Output: 3'''
