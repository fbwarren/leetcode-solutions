# [1706. Where Will the Ball Fall](https://leetcode.com/problems/where-will-the-ball-fall/)

**Main Idea**: Theres 4 cases that would stop a ball from falling. We can just follow the paths from top to bottom while checking for these cases.

**Algorithm**

A ball will get stuck on a cell in the following cases:

1. The cell is a 1 and the cell is either in the last column, or its neighbor to the right is a -1
2. The cell is a -1 and the cell either in the first column, or its neighbor to the left is a 1.

For each ball we are dropping, we start at the corresponding and then loop through each row. We check to see if any of the cases listed above occur, and if they don't, we move our ball to the right or the left depending on whether the cell we were just on was a 1 or a -1. At the end of each check, we update the output to reflect what column we're on (once the ball reaches the end, this update will leave the correct column in the output).

```python
def findBall(self, grid):
    output = [-1] * len(grid[0])
    numColumns = len(grid[0])

    for ball in range(len(output)):
        c = ball
        for r in range(len(grid)):
            if grid[r][c] == 1:
                if c >= numColumns-1 or grid[r][c+1] == -1:
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
```

**Time complexity**  
O(m*n) since in the worst case we'd have to check the entire column for all but one ball.

**Space complexity**  
O(n) where n is the number of balls.
