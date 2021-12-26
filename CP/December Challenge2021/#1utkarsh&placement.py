#by Nikhil Sharma on 3 Dec 2021
#@6:54pm solved
# UTKPLC

t = int(input())
for test_case in range(t):
    def preference():
        output = []
        for i in range(3):
            for j in range(2):
                if arr1[i] == arr2[j]:
                    output.append(arr1[i])
        return output[0]

    arr1 = list(input().split())
    arr2 = list(input().split())
    print(preference())