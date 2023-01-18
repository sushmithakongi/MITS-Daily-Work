def secondlar(list1):
    list2 = list(set(list1))
    list2.sort()
    return list2[-2]
list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
print("Second largest number is :",secondlar(list1))