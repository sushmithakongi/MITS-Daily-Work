'''Date:13/01/2023 Name:K Prasad Achari'''
'''Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ]
 where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, 
 S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first 
 ( with the least starting index).'''

def longestPalin(S):
    if len(S)==1:
        return S
    for i in range(len(S),0,-1):
        for j in range(len(S)-i+1):
            res=S[j:i+j]
            if res==res[::-1]:
                return res

S=input()
print(longestPalin(S))

'''Input:
S = "aaaabbaa"
Output: aabbaa'''