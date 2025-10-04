def Binary(BS):
    RV = ''
    for bs in BS:
        if bs == '0':
            RV += '1'
        if bs == '1':
            RV += '0'
    return RV

n = eval(input())
for i in range(n):
    b = input().strip()
    binary = Binary(b)
    binarys = int(binary, 2)
    print(f'{binarys+1:b}')