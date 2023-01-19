"""Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:
Input: nums = [1], k = 1
Output: [1]"""
#Source code
def topKFrequent(nums,k):
    cache = {}
    for num in nums:
        if num in cache:
            cache[num] += 1
        else: 
            cache[num] = 1
    cache = sorted(cache.items(), key=lambda x:x[1], reverse=True)
    return [cache[x][0] for x in range(k)]

nums = [1,1,1,2,2,3] 
k = 2
a = topKFrequent(nums,k)
print(a)