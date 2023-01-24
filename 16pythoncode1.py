'''Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j
Note :
i = 0,1.., m-1
j = 0,1, n-1 '''

row = int(input("enter rows: "))
col = int(input("enter columns: "))
multi_list = [[0 for j in range(col)] for i in range(row)]

for i in range(row):
    for j in range(col):
        multi_list[i][j]= i*j

print(multi_list)
