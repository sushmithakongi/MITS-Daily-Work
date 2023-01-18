'''Date:18/01/2023 Name:K Prasad Achari'''
'''Given a string S. The task is to print all unique permutations of the 
given string in lexicographically sorted order.'''

import itertools
def find_permutation(s):
    l=list(s)
    lis=[]
    res=[]
    for i in itertools.permutations(l):
        lis.append("".join(i))
    for i in lis:
        if i not in res:
            res.append(i)
    return sorted(res)

s=input()
print(find_permutation(s))

'''Input: ABC
Output:
ABC ACB BAC BCA CAB CBA'''

'''Input: ABSG
Output:
ABGS ABSG AGBS AGSB ASBG ASGB BAGS 
BASG BGAS BGSA BSAG BSGA GABS GASB 
GBAS GBSA GSAB GSBA SABG SAGB SBAG 
SBGA SGAB SGBA'''