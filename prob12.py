"""Compute the LCM of two given numbers using Python code."""
num_1 = 24   
num_2 = 92   
if num_1 > num_2: 
    greater_num = num_1    
else:   
    greater_num = num_2    
while(True):    
    if((greater_num % num_1 == 0) and (greater_num % num_2 == 0)):    
        lcm = greater_num  
        break    
greater_num += 1    
print("LCM of", num_1, "and", num_2, "=", greater_num)