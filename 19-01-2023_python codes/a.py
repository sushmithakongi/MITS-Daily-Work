# In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .
# You are given a string S . Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X,c) in the string.
# For a better understanding of the problem, check the explanation.
# Input Format
# A single line of input consisting of the string .
# Output Format
# A single line of output consisting of the modified string.
a=input()
l=[]
b=a[0]
c=1
for i in range(1,len(a)):
    if a[i]==b:
        c+=1
    else:
        l.append([c,int(b)])
        c=1
        b=a[i]
l.append([c,int(b)])
for i in l:
    print(tuple(i),end=' ')