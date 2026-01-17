n = input() # amount of lines to expect

def split_long_word(s):
    length = len(s)
    if len(s) > 10:
        return s[0] + str(length-2) + s[length-1]
    else: return s

for _ in range(n):
    print(split_long_word(input()))
        