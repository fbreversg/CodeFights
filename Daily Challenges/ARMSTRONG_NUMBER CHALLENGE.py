def Armstrong_number(N):
    check = 0
    for number in str(N):
        check += pow(int(number), len(str(N)))

    if N == check:
        return True
    else:
        return False

print (Armstrong_number(410))