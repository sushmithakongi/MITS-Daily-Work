def Find_median(arr,arr2,size,size2):
    m_size = size + size2
    merge_arr = [0]*m_size
    i=0
    k=0
    j=0
    while k<m_size:
       if i<size:
           merge_arr[k] = arr[i]
           i+=1
           k+=1

       if j<size2:
           merge_arr[k] = arr2[j]
           j+=1
           k+=1
    merge_arr.sort()
    if size % 2 == 1:
        median = merge_arr[size // 2]
        print("\nMedian= ", median)
    else:
        median = (merge_arr[m_size // 2] + (merge_arr[(m_size // 2) - 1])) / 2.0
        print("\nMedian= ", median)

arr=[]
arr2=[]
size = int(input("Enter the size of the 1st array: "))
size2 = int(input("Enter the size of the 2nd array: "))

print("Enter the Element of the 1st array:")
for i in range(0,size):
    num = int(input())
    arr.append(num)

print("Enter the Element of the 2nd array:")
for i in range(0,size2):
    num2 = int(input())
    arr2.append(num2)

Find_median(arr,arr2,size,size2)
