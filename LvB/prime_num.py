def IsPrime(oX):
    if oX % 2 == 0:
        return False
    else:
        for di in range(3, int(oX**0.5)+1, 2):
            if oX % di == 0:
                return False
        return True

k = eval(input())
for i in range(k):
    n = eval(input())
    if IsPrime(n):
        print(f"{n}: YES")
    else:
        print(f"{n}: NO")