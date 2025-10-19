N = eval(input())
for i in range(N):
    LS = input().split('|')
    STUDENT = []
    SCORE = []
    for ls in LS:
        STUDENT.append(ls.split(',')[0])
        SCORE.append(int(ls.split(',')[1]))
    sorted_score = sorted(SCORE)
    max = sorted_score[-1]
    min = sorted_score[0]
    max_name = STUDENT[SCORE.index(max)]
    min_name = STUDENT[SCORE.index(min)]
    if len(STUDENT) % 2 == 0:
        median = (sorted_score[(len(STUDENT)//2)-1] + sorted_score[(len(STUDENT)//2)]) / 2
    elif len(STUDENT) % 2 == 1:
        median = sorted_score[(len(STUDENT)//2)]
    print(f'{max}({max_name}),{min}({min_name}),{median:.1f}')
