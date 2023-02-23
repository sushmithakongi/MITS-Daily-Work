'''
Given two numbers a and b. In one operation you can pick any non negative 
integer x and either of a or b. Now if you picked a then replace a with 
a&x else if you picked b then replace b with b&x.
Return the minimum number of operation required to make a and b equal.
'''
#Input1:5
#12
#Output1:2
#Input2:5 5
#Output:0
class Solution:
    def solve(self,a,b):
        if a == b :
            return 0
        c1 = c2 = 0
        for i in range( 28 ) :
            if (a>>i)&1 == 1 and (b>>i&1) == 0 :
                c1 = 1
            if (a>>i)&1 == 0 and (b>>i)&1 == 1 :
                c2 = 1
        if c1 == c2 == 1 : return 2
        return 1
    
S=Solution()
print(S.solve(5,12))
print(S.solve(5,5))