'''
Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

'''
def longestCommonPrefix(strs):
    res = ""
    for a in zip(*strs):
        if len(set(a)) == 1: 
            res += a[0]
        else: 
            return res
    return res
strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))