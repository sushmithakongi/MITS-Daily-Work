''' Python3 code to demonstrate working of
Maximum occurring Substring from list'''
import re
import itertools

# initializing 
w_str = "gfghsisbjknlmkesbestgfgsdcngfgcsdjnisdjnlbestdjsklgfgcdsbestbnjdsgfgdbhisbhsbestdkgfgb"
w_list = ['is', 'best']

# printing original string and list
print("The original string is : " + w_str)
print("The original list is : " + str(w_list))

# Using regex() + groupby() + max() + lambda
seqs = re.findall(str.join('|', w_list), w_str)
grps = [(key, len(list(j))) for key, j in itertools.groupby(seqs)]
res = max(grps, key = lambda ele : ele[1])
		
# printing result
print("Maximum frequency substring : " + str(res[0]))