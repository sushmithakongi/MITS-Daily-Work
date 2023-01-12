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