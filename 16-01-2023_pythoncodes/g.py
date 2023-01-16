# There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.
# You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.
# A good path is a simple path that satisfies the following conditions:
# The starting node and the ending node have the same value.
# All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).
# Return the number of distinct good paths.
from collections import *
vals,edges=eval(input()),eval(input())
n = len(vals)
p = list(range(n))
count = [Counter({vals[i]:1}) for i in range(n)]
edges = sorted((max(vals[i],vals[j]),i,j) for i,j in edges)
res = n
def find(i):
    if p[i] != i:
        p[i] = find(p[i])
    return p[i]
for val, i, j in edges:
    pi, pj = find(i), find(j)
    res += count[pi][val]*count[pj][val]
    p[pi] = pj
    count[pj][val] += count[pi][val]
print(res)
#[1,3,2,1,3] [[0,1],[0,2],[2,3],[2,4]] 6