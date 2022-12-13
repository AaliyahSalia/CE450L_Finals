def primepair():
    primes = []
    for i in range(2, 1000):
        if isprime(i):
            primes.append(i)

    primepairs = []
    for i in range(len(primes) - 1):
        if primes[i + 1] - primes[i] == 2:
            primepairs.append((primes[i], primes[i + 1]))

    return primepairs

def isprime(n):
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
    
n = int(input("Enter a number less than 10000: "))
print("All pairs within input range:")
for pair in primepair():
    print("\t\t\t   %d %d" % pair)

