from math import ceil


test_case_count = int(input())
# read per line 3 things
for line in range(test_case_count):
    line_info = input()
    n,m,d = map(int, line_info.split())
    max_tower_height = (d//m) +1
    print(ceil(n/max_tower_height))
