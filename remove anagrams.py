""" Find Resultant Array After Removing Anagrams
You are given a 0-indexed string array words, where words[i] consists of lowercase English letters.
In one operation, select any index i such that 0 < i < words.length and words[i - 1] and words[i] are anagrams, and delete words[i] from words. Keep performing this operation as long as you can select an index that satisfies the conditions.
Return words after performing all operations. It can be shown that selecting the indices for each operation in any arbitrary order will lead to the same result.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase using all the original letters exactly once. For example, "dacb" is an anagram of "abdc".
Example 1:
Input: words = ["abba","baba","bbaa","cd","cd"]
Output: ["abba","cd"]
Example 2:
Input: words = ["a","b","c","d","e"]
Output: ["a","b","c","d","e"]"""

from collections import Counter


def removeAnagrams(words):
    res = [words[0]]
    for i in range(1, len(words)):
        mp1, mp2 = Counter(words[i-1]), Counter(words[i])
        if mp1 != mp2:
            res.append(words[i])
    return res


words = ["abba", "baba", "bbaa", "cd", "cd"]
a = removeAnagrams(words)
print(a)
