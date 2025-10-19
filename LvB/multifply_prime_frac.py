def IsPrime(x):
    if x == 2:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(2, int(x**0.5+1)):
            if x % i == 0:
                return False
    return True

K = eval(input())
for i in range(K):
    m = eval(input())
    PRIME = []
    for j in range(2, m+1):
        if IsPrime(j):
            PRIME.append(1/j)
    RV = 1
    for prime in PRIME:
        RV *= prime
    print(f'{RV:.3f}')
