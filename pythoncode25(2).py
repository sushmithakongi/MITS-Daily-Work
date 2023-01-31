'''Date:25/01/2023 Name:K Prasad Achari'''

'''Given a string s, return the longest palindromic substring in s.'''

def longestPalindrome(s):
    n = len(s)
    l = 0
    ans = ''
    for i in range(n):
        for j in range(i+1,n+1):
            if s[i:j] == s[i:j][::-1]:
                if (j-i) > l:
                    l = j-i
                    ans = s[i:j]
    return ans

s=input()
print(longestPalindrome(s))

'''Input:
s = "babad"
Output: "bab" '''

'''Input: 
s = "cbbd"
Output: "bb"'''