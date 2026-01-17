x = input()
def check(x):
    for char in x:
        if char in {"H", "Q", "9"}:
            return True
    return False

if (check(x)):
    print("YES")
else:
    print("NO")