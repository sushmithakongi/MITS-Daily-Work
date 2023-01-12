def generateParenthesis(n):
    res=[]
    def helper(s,no,nc):
        if no==0 and nc==0:
            res.append(s)
        elif no==nc:
            helper(s+"(",no-1,nc)
        elif no==0:
            helper(s+")",no,nc-1)
        else:
            helper(s+"(",no-1,nc)
            helper(s+")",no,nc-1)
    helper("",n,n)
    return res
print(generateParenthesis(3))
