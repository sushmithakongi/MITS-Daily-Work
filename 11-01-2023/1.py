<<<<<<< HEAD
'''You are required to implement the following function:
Int SumOddIntegers(int arr[], int n);
The function accepts an integer array ‘arr’ of length ‘n’ as its argument. You are required to 
calculate the sum of all odd integers in an array ‘an’ and return the same.
Note:
Array can have negative integers
n > 0
Computed values lie within integer range
Example:
Input:
arr: 1 4 6 7 10 12 11 5
n: 8
Output:
24
Explanation:
The odd integers in array {1, 4, 6, 7, 10, 12, 11, 5} are {1, 7,11, 5} and their sum is 24, hence 24 is 
'''

a=list(map(int,input()))
print(a[0::2])
=======
a=int(input())
for i in range(1,a+1):
    print(" "*(a-i)+(str(i)+' ') *i)
>>>>>>> 0f39cc0c6218d7bd3107c7a68e20741ac1262a6d
