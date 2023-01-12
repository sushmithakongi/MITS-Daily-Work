""" Maximum Product of Word Lengths
Given a string array words, return the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. If no such two words exist, return 0.
Example 1:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".
Example 2:
Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".
Example 3:
Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words."""
def maxProduct(words):
    ans = [0]
    letterSet = list(zip(words, [set(s) for s in words]))
    print(letterSet)
    for one in letterSet:
        for two in letterSet:
            if one[1].isdisjoint(two[1]):
                ans.append(len(one[0]) * len(two[0]))
    return max(ans)
a=maxProduct(["a","ab","abc","d","cd","bcd","abcd"])
print(a)