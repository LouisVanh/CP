n = int(input())
dividers = [7, 77, 777, 4, 44, 444, 47, 74, 774, 744, 447, 477]
def check(n):
    for div in dividers:
        if (n%div==0):
            return True
    return False

print("YES") if check(n) else print("NO")