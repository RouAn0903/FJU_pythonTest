k = eval(input())
for i in range(k):
    x = input()
    digits = x.replace('-', '')

    total = 0
    for j in range(12):
        num = int(digits[j])
        if j % 2 == 0 : #偶數位x1
            total += num*1
        else:           #奇數位x1
            total += num*3
    
    M = total % 10 
    N = 10 - M
    if N == 10:
        N = 0
    
    print(f"{x}-{N}")