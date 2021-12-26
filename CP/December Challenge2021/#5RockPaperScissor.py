def A(a,b):
    if a==b:
        return a
    elif (a=="R" and b=="P") or (a=="P" and b=="R"):
        return "P"
    elif (a=="P" and b=="S") or (a=="S" and b=="P"):
        return "S"
    else:
        return "R"

for i in range(int(input())):
    n=int(input())
    ans=[0]*n
    a=input()
    if n==1:
        print(a[0])
    else:
        r=[0]*n
        p=[0]*n
        s=[0]*n
        ch=""
        ans[n-1]=a[n-1]
        r[n-2]=A("R",a[n-1])
        p[n-2]=A("P", a[n - 1])
        s[n-2]=A("S", a[n - 1])
        if a[n-2]=="R":
            ans[n-2]=r[n-2]
        elif a[n-2]=="P":
            ans[n-2]=p[n-2]
        elif a[n-2]=="S":
            ans[n-2]=s[n-2]
        for i in range(n-3,-1,-1):
            temp=A("R",a[i+1])
            if temp=="R":
                r[i]=r[i+1]
            elif temp=="P":
                r[i]=p[i+1]
            else:
                r[i]=s[i+1]
            temp = A("P", a[i + 1])
            if temp == "R":
                p[i] = r[i + 1]
            elif temp == "P":
                p[i] = p[i + 1]
            else:
                p[i] = s[i + 1]
            temp = A("S", a[i + 1])
            if temp == "R":
                s[i] = r[i + 1]
            elif temp == "P":
                s[i] = p[i + 1]
            else:
                s[i] = s[i + 1]
            if a[i]=="R":
                ans[i]=r[i]
            elif a[i]=="P":
                ans[i]=p[i]
            else:
                ans[i]=s[i]
        print("".join(ans))