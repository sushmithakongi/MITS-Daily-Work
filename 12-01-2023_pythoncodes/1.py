# 1. Number of Nodes in the Sub-Tree With the Same Label
# You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 
# and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case 
# character given in the string labels (i.e. The node with the number i has the label labels[i]).
# The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.
# Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.
# A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.
from collections import *
n,edges,labels=int(input()),eval(input()),input()
tree = defaultdict(list)
for s,e in edges:
    tree[s].append(e)
    tree[e].append(s)
res = [0] * n
def dfs(node, par):
    count = Counter()
    for nei in tree[node]:
        if nei != par:
            count += dfs(nei, node)
    count[labels[node]] += 1
    res[node] = count[labels[node]]
    return count
dfs(0,-1)
print(res)
#n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"