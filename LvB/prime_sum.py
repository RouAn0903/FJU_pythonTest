def isPrime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

N = eval(input())
for i in range(N):
    m = int(input())
    total = 0
    for j in range(2, m+1):
        if isPrime(j):
            total += j
    print(total)