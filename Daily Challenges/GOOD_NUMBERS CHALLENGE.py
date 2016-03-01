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