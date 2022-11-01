def findBall(self, grid):
        output = [-1] * len(grid[0])
        rows, columns = len(grid), len(grid[0])

        for ball in range(len(output)):
            c = ball
            for r in range(len(grid)):
                if grid[r][c] == 1:
                    if c >= columns-1 or grid[r][c+1] == -1:
                        output[ball] = -1
                        break
                    c += 1
                else:
                    if c <= 0 or grid[r][c-1] == 1:
                        output[ball] = -1
                        break
                    c -= 1
                output[ball] = c

        return output
        