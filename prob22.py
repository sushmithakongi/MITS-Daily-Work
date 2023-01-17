"""Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"      """
def mul(s1,s2):
    res=int(s1)*int(s2)
    return res

def multiply(s1,s2):
        d1 = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9}
        d2 = {v:k for k,v in d1.items()}
        n1 = sum([d1[c]*(10**i) for i,c in enumerate(s1[::-1])])
        n2 = sum([d1[c]*(10**i) for i,c in enumerate(s2[::-1])])
        n3, s = n1*n2, ''
        while n3:
            s = d2[n3%10] + s
            n3 = n3//10
        return s if s else '0'

s1=input()
s2=input()
print(mul(s1,s2))
print(multiply(s1,s2))