while True:
    S = eval(input())
    if S == 0:
        break
    else:
        left, right = 1, 200000
        while left < right:
            mid = (left + right) // 2
            total = mid * (mid+1) // 2
            if total <= S:
                left = mid + 1
            else:
                right = mid
        n = left

        total_sum = n * (n+1) // 2
        missing_page = total_sum - S
        print(missing_page, n)