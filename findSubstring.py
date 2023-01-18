def findSubstring(s, words):
    ls=len(s)
    lw=len(words[0])
    start=0
    l=ls-lw+1
    rl=len(words)*lw
    d={}
    res=[]
    for w in words:
        if w in d:
            d[w]+=1
        else:
            d[w]=1
            
    while(start<l):
        nd={}
        for i in range(start,start+rl,lw):
            cs=s[i:i+lw]
            if cs in d:
                if cs in nd:
                    nd[cs]+=1
                else:
                    nd[cs]=1
                if nd==d:
                    res.append(start)
                    break
            else:
                break
        start+=1
            
    return res
print(findSubstring("barfoothefoobarman",["foo","bar"]))             
