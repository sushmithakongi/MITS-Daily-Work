'''
Generate Parentheses

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8

'''
def generateParenthesis(n):
    def helper(ans, s, left, right):
        if left==0 and right==0:
            ans.append(s)
                
        if left>0:
            helper(ans, s+'(', left-1, right)
                
        if right>0 and left<right:
            helper(ans, s+')', left, right-1)
        
    ans = []
    helper(ans, '', n, n)
    return ans
n = 3
print(generateParenthesis(n))