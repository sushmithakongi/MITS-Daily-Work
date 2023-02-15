def isMonotonic(A):
    ac = 0
    dc = 0
    for i in range(len(A) - 1):
        if (A[i] <= A[i + 1]):
            ac += 1
        if (A[i] >= A[i + 1]):
            dc += 11
    if ac == len(A) - 1 or dc == len(A) - 1:
        return True
    else:
        return False


A = list(map(int, input().split(",")))
print(isMonotonic(A))