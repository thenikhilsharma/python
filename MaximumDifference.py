n = int(input())

arr = list(map(int, input().split()))

mx = int(max(arr))
diff_arr = []

for i in range(len(arr)):
    diff = int(arr[i]) - mx
    diff_arr.append(diff)

mix = []

num = diff_arr
for i in num:
    if i < 0:
        i = -i
    mix.append(i)

print(max(mix))