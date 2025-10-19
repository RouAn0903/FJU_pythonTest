while True:
    n = eval(input())
    if n == 0:
        break
    else:
        LS = input().split(' ')
        Price = 0
        for i in range(0, len(LS), 2):
            Count = abs(int(LS[i+1])-int(LS[i]))
            if Count == 1 or Count == 2:
                Price += 20
            elif Count == 3:
                Price += 30
            elif Count == 4:
                Price += 40
        print(Price)