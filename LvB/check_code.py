def sum(X):
    count = 0
    for x in X:
        count += int(x)
    return count

while True:
    S = input()
    if S == '0':
        break
    else:
        RE = S
        while len(RE) > 1:
            RE = str(sum(RE))
        print(RE)