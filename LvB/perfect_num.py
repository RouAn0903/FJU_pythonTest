def IsProper(x):
    divisors = []
    for i in range(1,x):
        if x % i == 0:
            divisors.append(i)
    return divisors

K = eval(input())
for i in range(K):
    S = eval(input())
    if S == -1:
        break
    else:
        RE = IsProper(S)
        if sum(RE) == S:
            print('Perfect')
        elif sum(RE) < S:
            print('Deficient')
        else:
            print('Abundant')