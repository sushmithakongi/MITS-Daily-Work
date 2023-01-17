# Divide Two Integers
# Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means losing its fractional part. 
# For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store integers within 
# the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly 
# greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
d,di=int(input()),int(input())
positive = (d < 0) is (di < 0)
dividend, divisor = abs(d), abs(di)
res = 0
while dividend >= divisor:
    temp, i = divisor, 1
    while dividend >= temp:
        dividend -= temp
        res += i
        i <<= 1
        temp <<= 1
if not positive:
    res = -res
print(min(max(-2147483648, res), 2147483647))
 