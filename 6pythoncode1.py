""" is a shoe shop owner. His shop has  number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are  number of customers who are willing to pay  amount of money only if they get the shoe of their desired size.

Your task is to compute how much money  earned.
Sample Input

10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50
Sample Output

200"""
X = int(input()) 
shoes = list(map(int,input().split())) 
N = int(input()) 
sum = 0 
while N>0: 
    size,price = map(int,input().split()) 
    if size in shoes: 
        sum += price 
        shoes.remove(size) 
        N = N-1 
        print(sum)
        