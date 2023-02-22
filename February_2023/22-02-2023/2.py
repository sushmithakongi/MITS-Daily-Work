print("Enter the array:")
arr=list(map(int,input().split(',')))
print("Enter the element you want to found")
target=int(input())
flag=0
i=0
while i<len(arr):
    if arr[i]==target:
       index=i
       flag=1
    i+=1
if flag==0:
    print("The element is not found")
else:
    print("The element is found at ",index)