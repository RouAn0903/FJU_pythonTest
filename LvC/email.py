while True:
    m = input().strip()
    if m == '0':
        break

    if "@" not in m or "." not in m:
        print("False")
        continue

    at_index = m.find("@")
    dot_index = m.find(".")

    if at_index == 0:
        print("False")
        continue

    if dot_index < at_index:
        print("False")
        continue

    print("True")