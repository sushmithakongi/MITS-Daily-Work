# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] 
# represent the start and the end of the ith interval and intervals is sorted in ascending 
# order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending 
# order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.
from bisect import *
intervals,newInterval=eval(input()),eval(input())
insertI = bisect_left(intervals, newInterval)
intervals.insert(insertI, newInterval)
stack = []
for s,e in intervals:
    if stack and stack[-1][1] >= s:
        lastS,lastE = stack.pop()
        stack.append([lastS, max(lastE,e)])
    else:
        stack.append([s,e])
print(stack)
#intervals = [[1,3],[6,9]], newInterval = [2,5]