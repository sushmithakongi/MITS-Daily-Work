"""Uncommon Words from Two Sentences
A sentence is a string of single-space separated words where each word consists only of lowercase letters.
A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.
Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.
Example 1:
Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
Example 2:
Input: s1 = "apple apple", s2 = "banana"
Output: ["banana"]"""
def uncommonFromSentences(s1, s2):
        word_counts = {}
        for word in s1.split(' '):
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        for word in s2.split(' '):
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
        return [word for word in word_counts if word_counts[word] == 1]
s1 = "this apple is sweet"
s2 = "this apple is sour"
a=uncommonFromSentences(s1,s2)
print(a)
