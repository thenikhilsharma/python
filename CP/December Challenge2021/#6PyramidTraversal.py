#PYRAMID

from math import ceil, sqrt

display_modulo = 10 ** 9 + 7
max_factor = 10 ** 5
factors = [None] * (max_factor + 1)


def power_modulo(a, b, pow):
    a %= pow
    if a == 0:
        return 0
    prod = 1

    while (b > 0):
        if b % 2 == 1:
            prod *= a
            prod %= pow
            b -= 1
        a *= a
        a %= pow
        b //= 2

    return prod

def binom(n, k, p):
    return ((factors[n] * inv(factors[k], p) % p) * inv(factors[n - k], p)) % p


def inv(a, p):
    return power_modulo(a, p - 2, p)


def get_last_node(level):
    return ((level + 1) * level) // 2


def get_level_index_tuple(n):
    i = -1000
    l = -1000

    if n == 1:
        return (1, 1)

    finish = 1 + ceil(sqrt(n * 2))  # check if need to sign for long long somehow
    begin = 2

    while (begin <= finish):
        l = (begin + finish) // 2
        last = get_last_node(l)
        if (last >= n and get_last_node(l - 1) < n):
            break
        elif last > n:
            finish = l - 1
        else:
            begin = l + 1

    i = n - (l * (l - 1)) // 2
    return (l, i)


factors[0] = 1
factors[1] = 1

for i in range(2, max_factor + 1):
    factors[i] = factors[i - 1] * i % display_modulo


for _ in range(int(input())):
    s, e = map(int, input().split())
    t1 = get_level_index_tuple(s)
    t2 = get_level_index_tuple(e)

    res = -1000
    i_difference = t2[1] - t1[1]
    l_difference = t2[0] - t1[0]

    if l_difference <= 0 or i_difference < 0 or i_difference > l_difference:
        res = 0
    else:
        res = binom(l_difference, i_difference, display_modulo)

    print(res)