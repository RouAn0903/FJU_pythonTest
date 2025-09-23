n = eval(input())
for i in range(n):
    num = input().strip()   
    if 1000 <= int(num) <= 9999:
        # 檢查不同數字的數量
        if len(set(num)) == 2:
            # 檢查是否有連續相同的數字
            has_repeat = False
            for j in range(1, len(num)):
                if num[j] == num[j-1]:
                    has_repeat = True
                    break

            if not has_repeat:
                # 檢查至少有一個數字出現兩次以上
                d1, d2 = set(num)  # 拆出兩個不同的數字
                if num.count(d1) >= 2 or num.count(d2) >= 2:
                    print("Yes")
                else:
                    print("No")
            else:
                print("No")
        else:
            print("No")
    else:
        print("No")
