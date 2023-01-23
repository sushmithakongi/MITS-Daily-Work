"""Given the value of n(n < 10), i.e, number of lines, print the Fibonacci triangle.
Examples: 
Input : n = 5 
Output :
1 
1 2 
3 5 8 
13 21 34 55 
89 144 233 377 610 """
def fib(f, N):
	f[1] = 1
	f[2] = 1
	for i in range(3, N + 1):
		f[i] = f[i - 1] + f[i - 2]
def fiboTriangle(n):
	N = n * (n + 1) // 2
	f = [0] * (N + 1)
	fib(f, N)
	fiboNum = 1
	for i in range(1, n + 1):
		for j in range(1, i + 1):
			print(f[fiboNum], " ", end="")
			fiboNum = fiboNum + 1
		print()
n = int(input())
fiboTriangle(n)