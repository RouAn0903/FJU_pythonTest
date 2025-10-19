while True:
    LS = input().split(' ')
    if LS == ['0']:
        break
    else:
        ILS = []
        for ls in LS:
            ILS.append(int(ls))
        ILS = sorted(ILS, reverse=True)
        print(ILS)