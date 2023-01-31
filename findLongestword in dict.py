"""
Longest Word in Dictionary through Deleting
Given a string s and a string array dictionary, return the longest string in the dictionary that can be formed by deleting some of the given string characters. If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:

Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple"
Example 2:

Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"
 """
def findLongestWord(s,dictionary):
        def check(s: str, d: str) -> bool:
            it = iter(s)
            return all(l in it for l in d)
        m = ""
        for i in dictionary:
            if check(s, i) and (len(m) < len(i) or (len(m) == len(i) and m > i)):
                m = i
        return m 
s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
a=findLongestWord(s,dictionary)
print(a)