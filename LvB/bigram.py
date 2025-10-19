N = eval(input())
for i in range(N):
    S = input()
    BLS = []
    for j in range(len(S)-1):
        bs = S[j:j+2]
        if bs not in BLS:
            BLS.append(bs)
    print(len(BLS))