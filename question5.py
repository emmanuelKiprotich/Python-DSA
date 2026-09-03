x = 0
y = 20

while True:
    y = y - 4

    x = x + 2 / y

    if y < 6:
        break

print(f"x = {x}")
