K = eval(input())
for i in range(K):
    LS = input().split(' ')
    
    RS = []
    multiply = 1
    for ls in LS:
        multiply *= int(ls)
        RS.append(multiply)
    print(max(RS))