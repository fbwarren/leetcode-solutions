def orangesRotting(grid: List[List[int]]) -> int:
    queue = Deque()

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 2:
                queue.appendleft([r,c])

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

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                return -1

    return step
