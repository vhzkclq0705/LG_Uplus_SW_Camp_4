def roll_dice(a, b):
    if a % 2 == 1 and b % 2 == 1:
        return a * a + b * b
    elif a % 2 == 0 and b % 2 == 0:
        return abs(a - b)
    else:
        return 2 * (a + b)

a = int(input())
b = int(input())
print(roll_dice(a, b))