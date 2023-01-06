res = []
def getBinary(s):
    if "?" in s:
        s1 = s.replace('?', '0',1) 
        s2 = s.replace('?', '1', 1)
        getBinary  (s1)
        getBinary  (s2)
    else: 
        res.append(s)
s=input("string:-")     
getBinary(s)
print (res)