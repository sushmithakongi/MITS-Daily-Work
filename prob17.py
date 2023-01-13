"""The problem statement asks to produce a new list whose i^{th} element will be equal to the sum of the (i + 1) elements.
Input : list = [10, 20, 30, 40, 50]
Output : [10, 30, 60, 100, 150]"""
def Cumulative(lists):
    cu_list = []
    length = len(lists)
    cu_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return cu_list[1:]
lists = list(map(int, input().split()))
print (Cumulative(lists))
