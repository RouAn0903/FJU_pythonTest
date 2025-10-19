N = eval(input())
for i in range(N):
    S = input().upper().replace(' ','').replace(':','').replace('/','').replace("'",'')
    RV = S[::-1]
    if S == RV:
        print('Yes')
    else:
        print('No')