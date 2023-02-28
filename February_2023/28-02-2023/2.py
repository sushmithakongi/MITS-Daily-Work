# You are given a 0-indexed circular string array words and a string target. A circular array means that the array's end connects to the array's beginning.

# Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
# Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.

# Return the shortest distance needed to reach the string target. If the string target does not exist in words, return -1.


class Solution:
    def closetTarget(self, words, target, startIndex):
        if target not in words:
            return -1
        else:
            res1=abs((words.index(target)+1)-startIndex)
            res2=abs((words[::-1].index(target)+1)-startIndex)
            if res1<res2:
                return res1
            else:
                return res2

S=Solution()
print(S.closetTarget(["i","eat","leetcode"],"ate",0))
print(S.closetTarget(["a","b","leetcode"],"leetcode",0))


#Input:
# words =
# ["a","b","leetcode"]
# target =
# "leetcode"
# startIndex =
# 0
# Output:
# 1