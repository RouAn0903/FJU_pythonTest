N = eval(input())
for i in range(N):
    LS = input().split(' ')
    m = eval(LS[0])
    max = eval(LS[1])
    it = 1
    sum = it
    lastit = 0
    while sum <= max:
        lastit = it 
        it += m        # 每次加上公差 m
        sum += it      # 總和 sum 加上新的 it
    print(lastit)