#Count Odd Numbers in an Interval Range


#Regular method
def countOdds(low,high):
    c=0
    while low<=high:
        if low%2!=0:
            c+=1
        low+=1
    return c



#Effecient method or Maths method
def countOdds(low,high):
    if low%2==0 and high%2==0:
        return (high-low)//2
    else:
        return ((high-low)//2)+1
