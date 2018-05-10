def calculate(grid, visited, i, j):
    if (not(i in range(n) and j in range(m))):
        return 0
    if (grid[i][j] == 0 or visited[i][j] == 1):
        return 0
    path_length = 1
    visited[i][j] = 1
    path_length += calculate(grid, visited, i-1, j-1)
    path_length += calculate(grid, visited, i-1, j)
    path_length += calculate(grid, visited, i-1, j+1)
    path_length += calculate(grid, visited, i, j-1)
    path_length += calculate(grid, visited, i, j+1)
    path_length += calculate(grid, visited, i+1, j-1)
    path_length += calculate(grid, visited, i+1, j)
    path_length += calculate(grid, visited, i+1, j+1)
    return path_length

def getBiggestRegion(grid):
    longest_path = 0
    visited = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            path_length = calculate(grid, visited, i, j)
            if path_length > longest_path:
                longest_path = path_length
    return longest_path

n = int(input().strip())
m = int(input().strip())
grid = []
for grid_i in range(n):
    grid_t = list(map(int, input().strip().split(' ')))
    grid.append(grid_t)

print(getBiggestRegion(grid))
