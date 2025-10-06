n = eval(input())
for i in range(n):
    name = input().strip()
    if ',' in name:
        last, first = name.split(',')
        first = first.strip().split(' ')[-1]
        last = last.strip()
    else:
        first = name.split(' ')[0]
        last = name.split(' ')[-1]
    print(f"F={first} L={last}")