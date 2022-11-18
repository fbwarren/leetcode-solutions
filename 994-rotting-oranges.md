# [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

**Main Idea**  
Use BFS while keep track of how many bfs "steps" you've taken.

**Algorithm**  
We create a queue and add all of the initial rotting oranges.  
Then, we start bfs. We do BFS one "step" at a time so we can keep track of our steps. By one step, we process only the currently rotting oranges (the ones in the queue at the start at the step). We process a rotting orange by checking all of its neighbors. If a neighbor is a fresh orange, we mark it as rotting and add it to the queue to be processed in the next "step".  
At the end of each step, we increment the number of steps only if we actually made some new rotting oranges (i.e. the queue isn't empty).
Finally, bfs ends when the queue is empty (no more newly rotting oranges).  
We scan the grid one last time, returning -1 if there's any fresh oranges remaining.  
Otherwise, we return the step count.


```python
def orangesRotting(grid: List[List[int]]) -> int:
    queue = Deque()

    # Initial rotten oranges
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
                queue.appendleft([r,c])

    # bfs
    step = 0
    dirs = (0, 1, 0, -1, 0)
    while queue:
        for _ in range(len(queue)):
            r, c = queue.pop()
            for i in range(4):
                newR, newC = r + dirs[i], c + dirs[i+1]
                if (0 <= newR < len(grid)) and (0 <= newC < len(grid[0])):
                    if grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        queue.appendleft([newR, newC])
        if len(queue):
            step += 1

    # final scan
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                return -1

    return step
```

**Time complexity**  
$O(m \times n)$ because we visit each cell at most once

**Space complexity**  
$O(m \times n)$ because our queue could potentially hold $m \times n$
