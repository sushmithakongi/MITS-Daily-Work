'''
Python | Check if a Substring is Present in a Given String
Example 1: Input : Substring = "geeks" 
           String="geeks for geeks"
Output : yes
Example 2: Input : Substring = "geek"
           String="geeks for geeks"
Output : yes
'''

def substringpresent(string,substring):
    s = string.split()
    if substring in s:
        return "yes"
    else:
        return "no"
string = "python is very easy"  
substring = "eay"
print(substringpresent(string,substring)) 