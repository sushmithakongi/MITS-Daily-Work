""" Longest Word in Dictionary
Given an array of strings words representing an English Dictionary, return the longest word in words that can be built one character at a time by other words in words.
If there is more than one possible answer, return the longest word with the smallest lexicographical order. If there is no answer, return the empty string.
Note that the word should be built from left to right with each additional character being added to the end of a previous word. 
Example 1:
Input: words = ["w","wo","wor","worl","world"]
Output: "world"
Explanation: The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
Example 2:
Input: words = ["a","banana","app","appl","ap","apply","apple"]
Output: "apple"
Explanation: Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply"."""
def longestWord(words):
        words.sort()
        ans = ''
        contains = set([''])
        for word in words:
            if word[:-1] in contains:
                contains.add(word)
                if len(word) > len(ans):
                    ans = word
        return ans
words = ["w","wo","wor","worl","world"]
a=longestWord(words)
print(a)