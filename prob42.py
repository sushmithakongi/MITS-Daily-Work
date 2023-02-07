"""There are given two strings 
 and 
 consisting of lowercase English letters, both of same length. Let’s say length of both strings is 

Sample Input
pcabb
bbacp
Sample Output
YES"""
t=input() 
s=input() 
res=[] 
for i in t: 
    if i in s: 
        v=i 
        res.append(v) 
if(res==s): 
    print("YES") 
else: 
    print("NO")