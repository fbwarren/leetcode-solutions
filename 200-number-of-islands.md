# [200. Number of Islands](https://leetcode.com/problems/number-of-islands/)

**Main Idea**  DFS

**Algorithm**  
Iterate through the grid. When you find a "1", increment your island count and perform DFS to find and mark all parts of the island.  
Visiting a cell in DFS consists of marking it seen and checking each of the four neighbors to see if they are also land.

```python
def numIslands(grid: List[List[str]]) -> int:
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
```

**Time complexity**  
$O(n)$ since we only visit each cell at most twice. (Consider the case where the entire grid is land.)

**Space complexity**  
$O(1)$ since we don't have any variable length data structures.
