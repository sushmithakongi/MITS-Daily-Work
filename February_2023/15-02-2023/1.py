'''You are given  words. Some words may repeat.
For each word, output its number of occurrences.
The output order should correspond with the input order of appearance of the word.
See the sample input/output for clarification.'''

d={}
l=[]
n=int(input())
i=0
res=[]
while(i<n):
    l.append(input())
    i+=1
for word in l:
    d[word]=d.get(word,0)+1
print(len(d))
for value in d.values():
    res.append(value)
print(*sorted(res,reverse=True))

'''
Input:
4
bcdef
abcdefg
bcde
bcdef
Output:
3
2 1 1
'''