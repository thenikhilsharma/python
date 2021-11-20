T = int(input()) #no of test cases
final_order = []
final_input = []

for i in range(1, T+1):
    inputs = list(input().split())
    S = list(input().split()) # order of dogs and cats

    final_order.append(S)
    final_input.append(inputs)

for j in range(T):
    N = int(final_input[j][0])
    D = int(final_input[j][1])
    C = int(final_input[j][2])
    M = int(final_input[j][3])
    Z = 1

    str1 = " "
    zanchu = str1.join(final_order[j])
    final = list(zanchu)
    DA = 0

    for da in range(len(zanchu)):
        if final[da] == "D":
            DA = DA+1
    if DA != 0:
        for k in range(len(zanchu)):
            if final[k] == "C"and C>=0:
                C = C-1
            elif final[k] == "D" and D>=0:
                D = D-1
                C = C+M
            if C <0 or D<0:
                print("Case #",j+1,": NO",sep="")
                Z = 0
                break
        if C>=0 and D>=0 and Z != 0:
            print("Case #",j+1,": YES",sep="")
    else:
        print("Case #",j+1,": YES",sep="")