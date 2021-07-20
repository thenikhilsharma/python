def staircase(num_stairs):
    n = num_stairs - 1
    for stairs in range(num_stairs):
        print (' ' * n, '#' * stairs)
        n -= 1
    print ('#' * num_stairs)

n = int(input())

staircase(n)