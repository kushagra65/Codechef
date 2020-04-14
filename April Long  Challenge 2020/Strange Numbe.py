# A function to print all prime factors of
# a given number n
import math
def primeFactors(n):
    # Print the number of two's that divide n
    count=0
    while n % 2 == 0:
        count+=1
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    for i in range(3, int(math.sqrt(n)) + 1, 2):

        # while i divides n , print i ad divide n
        while n % i == 0:
            count+=1
            n = n / i

            # Condition if n is a prime
    # number greater than 2
    if n > 2:
        count+=1
    return count


if __name__ == '__main__':
    count = 0
    for i in range(int(input())):
        N, K = map(int,input().split())
        x=primeFactors(N)
        if x>=K:
            print(1)
        else:
            print(0)

