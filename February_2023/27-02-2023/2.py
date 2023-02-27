#Given an array Arr of N positive integers and another number X. Determine whether or not there exist two elements in Arr whose sum is exactly X.

class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
		for ele in arr:
		    if ele-n in arr:
		        return "Yes"
		    else:
		        return "No"

S=Solution()
print(S.hasArrayTwoCandidates([1,4,45,6,10,8],6,16))

#Input:
#N = 6, X = 16
#Arr[] = {1, 4, 45, 6, 10, 8}
#Output: Yes