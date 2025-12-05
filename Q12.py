x = 0
y = 0
while True:
    print(x, y)
    if x == 2 or y == 2:
        print("Goal reached!")
        break
    if x == 0:
        x = 4
    elif y == 3:
        y = 0
    else:
        transfer = min(x, 3 - y)
        x -= transfer
        y += transfer