'''
python program to print the following pattern

     1
    222
   33333
  4444444
 555555555
66666666666
'''

n=int(input("Enter num of rows: "))
for i in range(1, n+1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(2 * i - 1):
        print(i, end='')
    print()