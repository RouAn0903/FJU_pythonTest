RC = input().split(' ')
R = int(RC[0])
C = int(RC[1])

A = []
for i in range(R):
    a = input().split(' ')
    A.append(a)

for c in range(C):
    co = ''
    for r in range(R):
        if co == '':
            co = A[r][c]
        else:
            co += (' ' + A[r][c])
    print(co)            
