"""Find Common Characters
Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.
Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]"""
from collections import Counter
def commonChars(words):
        ans = Counter(words[0])
        for i in range(1, len(words)):
            ans &= Counter(words[i])
        return list(ans.elements())
words = ["bella","label","roller"]
a=commonChars(words)
print(a)