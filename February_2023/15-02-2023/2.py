'''deque operations'''
from collections import deque
d=deque()
for i in range(int(input())):
    a=input()
    if a[:7]=='append':
        d.append(int(a[-1]))
    if a[:10]=='appendleft':
        d.appendleft(int(a[-1]))
    if a[:3]=='pop':
        d.pop()
    if a[:7]=='popleft':
        d.popleft()
print(*d)

'''
Input:
6
append 1
append 2
append 3
appendleft 4
pop
popleft
-------------
Output:
1 2
'''