'''Date : 06/02/2023 Name : K Prasad Achari'''

'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go 
outside the signed 32-bit integer range [-231, 231 - 1], then return 0.'''

def reverse(x):
    result = str(x)[::-1]
    # If the string contains '-', remove it and
    # place it at beggining of the string
    if result[len(result) - 1] == '-':
        result = result[:-1]
        result = '-' + result
    # Convert to int to remove any '0' chars
    result = int(result)
    # Check 32-bit int constraints and return string
    if (-2 ** 31) <= result <= (2 ** 31) - 1:
        return str(result)
    return 0

x=int(input())
print(reverse(x))

'''Input: x = 123
Output: 321'''
'''Input: x = -123
Output: -321'''
'''Input: x = 120
Output: 21'''

