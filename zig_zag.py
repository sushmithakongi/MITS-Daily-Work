def convert(s: str, numRows: int) -> str:
    if numRows==1:
        return s
    down=1
    res=["" for _ in range(numRows)]
    row=0
    for ch in s:
        res[row]+=ch
        if row+1==numRows:
            down=0
        elif row==0:
            down=1
        if down==1:
            row+=1
        else:
            row-=1
    return "".join(res)
print(convert("PAYPALISHIRING",3))

