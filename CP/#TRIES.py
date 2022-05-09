import sys, math

sys.stdout = open('D:\\git repository\\thenikhilsharma_python\\CP\\output.txt', 'w')
sys.stdin = open('D:\\git repository\\thenikhilsharma_python\\CP\\input.txt', 'r')

def find_ans():
    minimum_list = [cyan_min, magenta_min, yellow_min, black_min]
    minimum_list_sum = sum(minimum_list)
    minimum_of_minimum_list = minimum_list.index(min(minimum_list))
    maximum_of_minimum_list = minimum_list.index(max(minimum_list))

    if minimum_list_sum == 10**6:
        return minimum_list
    else:
        difference = minimum_list_sum-(10**6)
        ans = minimum_list
        ans[minimum_of_minimum_list] = minimum_list[minimum_of_minimum_list]
        if minimum_list[maximum_of_minimum_list]-difference > 0:
            ans[maximum_of_minimum_list] = minimum_list[maximum_of_minimum_list]-difference
        elif difference // 2 > 0:
            difference = difference // 2
 
        return ans

for tc in range(int(input())):
    printer_1 = list(map(int, input().split()))
    printer_2 = list(map(int, input().split()))
    printer_3 = list(map(int, input().split()))

    cyan    =   [printer_1[0], printer_2[0], printer_3[0]]
    magenta =   [printer_1[1], printer_2[1], printer_3[1]]
    yellow  =   [printer_1[2], printer_2[2], printer_3[2]]
    black   =   [printer_1[3], printer_2[3], printer_3[3]]

    cyan_min    = min(cyan)
    magenta_min = min(magenta)
    yellow_min  = min(yellow)
    black_min   = min(black)

    if 0 in printer_1 or 0 in printer_2 or 0 in printer_3:
        print('Case #%d: %s' %(tc+1, 'IMPOSSIBLE'))
    elif sum([cyan_min, magenta_min, yellow_min, black_min]) < 10**6:
        print('Case #%d: %s' %(tc+1, 'IMPOSSIBLE'))
    else:
        ans_list = find_ans()
        print('Case #',tc+1,': ',ans_list[0],' ', ans_list[1], ' ', ans_list[2], ' ', ans_list[3], sep='')
