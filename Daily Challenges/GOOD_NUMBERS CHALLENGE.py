"""
We will call an integer N good if either 5 * N2 - 4 or 5 * N2 + 4 is an exact square of an integer. You are given an array of requests, where each request is an integer given as a string.

Return an array of responses, such that for each i the ith element of the answer is the requestith good integer.

Example:

good_numbers(["1", "2", "3"]) = [1, 2, 3].
The first good number is 1, the second is 2, and the third is 3.
good_numbers(["4"]) = [5].
The fourth good number is 5.
[input] array.string requests

1 ≤ requests.size() ≤ 100
1 ≤ requests[i] ≤ 1018
[output] array.integer

Array of integers, such that its ith element is the requestith good integer.
"""

import math

def is_square(integer):
    try:
        root = math.sqrt(integer)
        if int(root + 0.5) ** 2 == integer:
            return True
        else:
            return False
    except ValueError:
        return False

def good_numbers(requests):

    temp = []
    result = []

    i=1
    while len(temp) < max([int(i) for i in requests]):
        good1 = 5 * pow(int(i), 2) - 4
        good2 = 5 * pow(int(i), 2) + 4

        if is_square(good1) or is_square(good2):
            temp.append(i)

        i += 1

    for item in requests:

        result.append(temp[int(item)-1])

    return result

bla = good_numbers(["1",
 "2",
 "3",
 "4",
 "5",
 "6",
 "7",
 "8",
 "9",
 "10",
])

print(bla)