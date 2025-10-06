n = eval(input())
for i in range(n):
    S = input().split(' ')
    a = eval(S[0])
    b = eval(S[1])
    c = eval(S[2])
    s = eval(S[3])
    
    # 計算三人年齡
    x3 = (20 + s - b - c) / 3  # 小來
    x2 = x3 + b                # 小起
    x1 = x3 + c                # 小華

    print(f"{int(x1)} {int(x2)} {int(x3)}")