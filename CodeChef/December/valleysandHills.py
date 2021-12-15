#completed
t = int(input())
for tc in range(t):
    hills, valleys = map(int, input().split())
    if valleys > hills:
        terrain = '10'*(hills+1) + '110'*(valleys - hills - 1) + '1'
    elif hills > valleys:
        terrain = '01'*(valleys+1) + '001'*(hills - valleys - 1) + '0'
    else:
        terrain = '01' * hills
    print(len(terrain))
    print(terrain)