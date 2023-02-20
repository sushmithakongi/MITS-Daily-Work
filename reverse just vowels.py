"""Reverse Vowels of a String
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Example 1:
Input: s = "hello"
Output: "holle"
Example 2:
Input: s = "leetcode"
Output: "leotcede" """


def reverseVowels(s):
    q = []
    n = ['a', 'i', 'e', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for i in s:
        if i in n:
            q.append(i)
            s = s.replace(i, '*')
    q.reverse()
    k = 0
    for i in s:
        if i == "*":
            s = s.replace("*", q[k], 1)
            k = k+1
    return s


s = "leetcode"
a = reverseVowels(s)
print(a)
