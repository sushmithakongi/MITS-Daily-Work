class Solution:
    def getMinDiff(self, arr, n, k):
        arr.sort()
        ans = arr[n-1] - arr[0]
        
        smallest = arr[0]+k
        largest = arr[n-1]-k
        
        for i in range(n-1):
            mi = min(smallest, arr[i+1]-k)
            ma = max(largest, arr[i]+k)
            if mi < 0:
                continue
            ans = min(ans, (ma-mi))
        return ans