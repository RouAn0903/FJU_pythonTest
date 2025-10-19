N = eval(input())
names = []
for i in range(N):
    S = input()
    names.append(S)
    # 排序:先按照長度，再按字母順序
    names.sort(key=lambda x: (len(x), x))
for name in names:
    print(name)