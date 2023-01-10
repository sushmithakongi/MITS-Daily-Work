"""Given three numbers x, y and p, compute (xy) % p. 
Examples : 
Input:  x = 2, y = 3, p = 5
Output: 3
Explanation: 2^3 % 5 = 8 % 5 = 3."""
def power(x, y, p):
    res = 1
    while (y > 0):
        if ((y & 1) != 0):
            res = res * x
        y = y >> 1  
        x = x * x 
    return res % p
x=int(input())
y=int(input())
p=int(input())
print(power(x,y,p))