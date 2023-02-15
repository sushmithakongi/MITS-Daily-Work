#to remove duplicates
n = input("enter the input elements : ")
list = n.split()
new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
print("output : ",*new_list)