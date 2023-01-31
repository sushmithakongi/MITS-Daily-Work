'''1.Longest Valid Parenthesis

Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses 
substring.

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ') '''


def findMaxLen(string):
	n = len(string)
	stk = []
	stk.append(-1)
	result = 0
	for i in range(n):

		if string[i] == '(':
			stk.append(i)
			
		else:
			if len(stk) != 0:
				stk.pop()

			if len(stk) != 0:
				result = max(result,
							i - stk[len(stk)-1])
				
			else:
				stk.append(i)

	return result

string = "((()()"
print (findMaxLen(string))

string = "()(()))))"
print (findMaxLen(string))
