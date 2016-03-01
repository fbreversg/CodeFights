import math

memoFact = {}

#Given N, return smallest M which divides factorial(N)
def smallest(N):

    M = 2
    while True:
        if M in memoFact:
            factM = memoFact[M]
        else:
            factM = math.factorial(M)
            memoFact[M] = factM

        if factM % N == 0:
            return M
        else:
            M += 1

def divisibilityOfFactorials(N):
    sums = 0
    for counter in range (2, N+1):
        temp = smallest(counter)
        sums += temp

    return sums

print (divisibilityOfFactorials(100))