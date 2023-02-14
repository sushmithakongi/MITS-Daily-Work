'''Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go 
outside the signed 32-bit integer range [-231, 231 - 1], then return 0.'''

def reverse(x):
    result = str(x)[::-1]
    if result[len(result) - 1] == '-':
        result = result[:-1]
        result = '-' + result
    result = int(result)
    if (-2 ** 31) <= result <= (2 ** 31) - 1:
        return str(result)
    return 0

x=int(input())
print(reverse(x))


