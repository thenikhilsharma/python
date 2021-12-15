#back tracking for rat maze
ratMaze = [
    [1,0,0,0,0,1],
    [1,1,1,1,0,1],
    [1,0,1,0,0,0],
    [1,1,1,0,0,0],
    [1,0,1,0,0,0],
    [0,0,1,1,1,1]
]

initial_pos_x, initial_pos_y = map(int, input().split())
exit_x, exit_y = map(int, input().split())
solArr = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]
solArr[initial_pos_x][initial_pos_y] = 1

def validMove(maze, x, y):
    print(x, y)
    if x == exit_x and y == exit_y: return solArr
    else:
        if y != len(maze[x]) and maze[x][y+1] == 1:
            solArr[x][y+1] = 1
            return validMove(maze, x, y+1)

        elif x != len(maze) and maze[x+1][y] == 1:
            solArr[x+1][y] = 1
            return validMove(maze, x+1, y)

        elif y != len(maze[x]) and maze[x][y+1] == 0:
            maze[x][y] = 0
            solArr[x][y] = 0
            return validMove(maze, x, y-1)

        elif x != len(maze) and maze[x+1][y] == 0:
            maze[x][y] = 0
            solArr[x][y] = 0
            return validMove(maze, x-1, y)

solArr = validMove(ratMaze, initial_pos_x, initial_pos_x)
for i in solArr:
    print(i)