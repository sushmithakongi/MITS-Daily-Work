"""Write a Python program that rotates an array by two positions to the right."""
listt = [23, 12, 5, 24, 23, 76, 86, 24, 86, 24, 75] 
for _ in range(0,2):  
    temp = listt[len(listt)-1]  
    for i in range(len(listt)-1,-1,-1):  
        listt[i]=listt[i-1]  
        listt[0]=temp  
print("After implementing right rotation the list is :")  
print(listt)  