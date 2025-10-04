import datetime

n = int(input())
for i in range(n):
    y, m, d = map(int, input().split())
    # 建立日期物件
    date = datetime.date(y, m, d)
    base = datetime.date(2000, 1, 1)  # 基準日
    
    days = (date - base).days + 1     # 計算相差天數 (含當天)
    week = (days + 4) % 7 + 1         # 2000/1/1 是星期六 → 對應 week=6
    print(week)