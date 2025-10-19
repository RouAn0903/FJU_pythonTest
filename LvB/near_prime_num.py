def CheckP(x):
    for k in range(2, int(x**0.5)+1):
        if k > 2 and k % 2 == 0:
            continue
        elif x % k == 0:
            return False
    return True


while True:
    num = eval(input())
    if num <= 1:
        break
    else:
        i = 2  # check P
        LastP = -1
        NextP = -1
        while True:
            # check i IsP or not
            if CheckP(i):
                if i < num:
                    LastP = i
                if i > num:
                    NextP = i
                    break
            i += 1
        print(f'{LastP} {NextP}')
