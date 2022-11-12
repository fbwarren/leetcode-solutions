def numIslands(self, grid: List[List[str]]) -> int:
    def dfs(r, c):
        grid[r][c] = 0
        for i in range(4):
            new_r,new_c = r + directions[i], c + directions[i+1]
            if (0 <= new_r < len(grid)) and (0 <= new_c < len(grid[0])) and grid[new_r][new_c] == "1":
                dfs(new_r, new_c)

    directions = (0, 1, 0, -1, 0)
    output = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == "1":
                output += 1
                dfs(r, c)

    return output
