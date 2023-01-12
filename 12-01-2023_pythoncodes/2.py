#2. minimize the sum
# You are given N elements, you can remove any two elements from the list, note their sum, and 
# add the sum to the list. Repeat these steps while there is more than a single element in the list.
# The task is to minimize the sum of these chosen sums.
# Example 1:
# Input:
# N = 4
# arr[] = {1, 4, 7, 10}
# Output:
# 39
import heapq
N,arr=int(input()),list(map(int,input().split()))
heapq.heapify(arr)
su=0
while(len(arr)>1):
    f=heapq.heappop(arr)
    s=heapq.heappop(arr)
    su=su+f+s
    heapq.heappush(arr,f+s)
print(su)