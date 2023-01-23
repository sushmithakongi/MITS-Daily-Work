def calculateTax(brackets,income):
    res=0
    if income==0:
        return 0
    if income>=brackets[0][0]:
        res=brackets[0][0]*brackets[0][1]/100
    else:
        return income*brackets[0][1]/100
            
        
    for i in range(1,len(brackets)):
        if brackets[i][0]>=income:
            amt=income
            res+=(amt-brackets[i-1][0])*brackets[i][1]/100
            break
        else:
            res+=(brackets[i][0]-brackets[i-1][0])*brackets[i][1]/100
            
    return res
print(calculateTax([[3,50],[7,10],[12,25]],10))
