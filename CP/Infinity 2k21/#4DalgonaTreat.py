#DALGONA

for m in range(int(input())):
    n=int(input())
    if n==1:
        print("1\n1 1")
    elif n==2:
        print("2\n3 1\n4 1")
    elif n==4:
        print("1\n2",n)
    else:
        print(2)
        print('2',n-1)
        print(n-2,'1')