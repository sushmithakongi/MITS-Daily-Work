""" Reverse Only Letters
Given a string s, reverse the string according to the following rules:
All the characters that are not English letters remain in the same position.
All the English letters (lowercase or uppercase) should be reversed.
Return s after reversing it.
Example 1:
Input: s = "ab-cd"
Output: "dc-ba"
Example 2:
Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"
Example 3:
Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!" """
def reverseOnlyLetters(s):
        stack = [c for c in s if c.isalpha()]
        return "".join(stack.pop() if c.isalpha() else c for c in s)
s = "Test1ng-Leet=code-Q!"
a=reverseOnlyLetters(s)
print(a)