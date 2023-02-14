st="""
StudentA : 67 
StudentB : 90
StudentC : 86
StudentD : 7
StudentE : 54
"""


a = st.split("\n")
t=40
for i in a:
    b=i.split(":")
    if len(b)<2:
        continue
    if  len(b)==2 and  int(b[1])>t:
        print(b[0]+ "is pass")
    else:
        print(b[0]+ "is fail")