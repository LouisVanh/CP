n = int(input()) #n lines of code

x,y,z = 0,0,0
for _ in range(n):
    new_x, new_y, new_z = input().split()
    x+=int(new_x)
    y+=int(new_y)
    z+=int(new_z)

if(x==0 and y==0 and z==0): print("YES")
else: print("NO")