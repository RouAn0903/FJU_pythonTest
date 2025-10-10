LS = input().split(' ')
N = int(LS[0])
RLS = []
DescLS = []
AscLS = []

for i in range(1, len(LS)-1):
    AbsV = abs(eval(LS[i])-eval(LS[i+1]))  # abs() => 絕對值
    RLS.append(AbsV)
    DescLS.append(N-i)
    AscLS.append(i)

if RLS == DescLS:
    print('Jolly')
elif RLS == AscLS:
    print('Jolly')
else:
    print('Not jolly')