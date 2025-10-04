n = eval(input())
for i in range(n):
    total_s = eval(input())
    s = total_s % 60
    total_m = total_s // 60
    m = total_m % 60
    h =  total_m // 60
    print(f'{h:0>2}:{m:0>2}:{s:0>2}')