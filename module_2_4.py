numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
for i in range(1,len(numbers)):
    for j in range(1,len(numbers)):
        if i > 1:
            if (i / j) == 0 and (i / j) == i:
                primes.append(i)
            else:
                not_primes.append(i)
print(set(primes))
print(set(not_primes))
