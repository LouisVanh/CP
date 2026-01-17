n, k = input().split()
n, k = int(n), int(k) - 1

# TLE
# lst = []
# def build_odd(n):
#     for x in range(n+1):
#         if x%2!=0: #odd
#             lst.append(x)

# def build_even(n):
#     for x in range(1,n):
#         if x%2==0: #even
#             lst.append(x)

#build_odd(n)
#build_even(n)
#print(lst)
#print(lst[k-1])
# if (k > n//2):
# als n even is, dan zijn de eerste n/2 elementen allemaal oneven
# 1 3 5 7 9 | 2 4 6 8 10
if(n%2==0):
    even_vanaf = n//2
    if(k<even_vanaf): #oneven gedeelte: getal x vind je met formule 1 + k*2
        print(1 + 2*k)
    else: # k >= even gedeelte: getal x vind je met formule k-(n/2) * 2
        print((1 + (k-even_vanaf)) * 2)

# als n oneven is, dan zijn de eerste n//2 + 1 elementen allemaal oneven
# 1 3 5 7 9 | 2 4 6 8
else:
    even_vanaf = n//2 +1
    if(k<even_vanaf): #oneven gedeelte: getal x vind je met formule 1 + k*2
        print(1 + 2*k)
    else: # k >= even gedeelte: getal x vind je met formule k-(n/2) * 2
        print((1 + (k-even_vanaf)) * 2)

