#to print prime number series
n = int(input())
for num in range(2,n+1):
    count = 0
    for j in range(1,num+1):
        if num%j==0:
            count += 1
    if count==2:
        print(num,end=" ")
