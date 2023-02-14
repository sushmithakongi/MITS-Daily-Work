n = int(input("enter first value :"))
x = int(input("enter second value :"))
for num in range(n,x+1):
    count = 0
    for j in range(1,x+1):
        if(num % j==0):
            count=count+1
    if(count==2):
        print(num,end=" ")