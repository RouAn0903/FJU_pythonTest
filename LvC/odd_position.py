n = eval(input())
for i in range(n):
    num = eval(input())
    b = bin(num)[2:]
    d = b.count('1')
    if d % 2 == 1:
        print(f"{num}: YES")
    else:
        print(f"{num}: NO") 