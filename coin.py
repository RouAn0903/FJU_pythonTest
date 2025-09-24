while True:

    money = eval(input())
    if money == 0:
        break
    
    c50 = money // 50
    money %= 50
    c10 = money // 10
    money %= 10
    c5 = money // 5
    money %= 5 
    print(f'{c50} {c10} {c5} {money}')



