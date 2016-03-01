"""
An Armstrong number is a number that is the sum of its own digits each raised to the power of the number of digits.
Check if the given number is an Armstrong number.

Example:

Armstrong_number(407) = true
43 + 03 + 73 = 64 + 343 = 407.
Armstrong_number(23) = false
22 + 32 = 13 ≠ 23.
[input] integer N

1 ≤ N ≤ 109
[output] boolean

true is the given number is an Armstrong number, false otherwise.
"""

def Armstrong_number(N):
    check = 0
    for number in str(N):
        check += pow(int(number), len(str(N)))

    if N == check:
        return True
    else:
        return False

print (Armstrong_number(410))