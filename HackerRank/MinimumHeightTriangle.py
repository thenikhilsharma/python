arr = list(map(int, input().split()))

b = arr[0]
a = arr[1] * 2

h = a / b

if h%1 < 0.5 and h%1 > 0.0:
    h = round(h+1)
    print(h)
elif h%1 > 0.5:
    h = round(h)
    print(h)
else:
    print(int(h))