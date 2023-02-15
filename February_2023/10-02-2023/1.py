"""Given two binary strings a and b, return their
sum as a binary string using inbuilt functions"""


def addBinary(a: str, b: str):
    c=int(a,2)+int(b,2)
    res=str(bin(c))
    return res[2:]

print(addBinary("11","1"))#100
print(addBinary("1010","1011"))#10101