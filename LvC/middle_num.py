n = eval(input())
for i in range(n):
    num = input().split(' ')
    num_sort = sorted(num, key=int)
    print(num_sort[1])