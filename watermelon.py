x = int(input())
def check(n):
    if (n % 2 == 0 and n > 2): return "YES"
    else: return "NO"

print(check(x))