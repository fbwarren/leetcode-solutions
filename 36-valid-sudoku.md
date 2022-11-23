# [36. Valid Sudoku](https://leetcode.com/problems/valid-sudoku/)

**Main Idea**  
Loop through the cells, check if we've seen that number in its respective row, column, and 3x3 square.

**Algorithm**  
We'll use 3 hash maps to keep track of the numbers we've seen in each row/column/square. Each hash map's keys are the row's/column's/square's index. The keys point to a set of seen numbers for that particular row/column/square.  
We loop through all the cells just once. If a cell is a number, we check each hashmap to see if we've already seen that number for that row/column/square. If so, we return False. Otherwise, we add the number to each hashmap's set.  
We return True if we've looped through the cells without returning False.

```python
def isValidSudoku(board: List[List[str]]) -> bool:
    rows = {i: set() for i in range(9)}
    cols = {i: set() for i in range(9)}
    squares = {i: set() for i in range(9)}

    for r in range(len(board)):
        for c in range(len(board[0])):
            cell = board[r][c]
            square = 3 * (r // 3) + (c // 3)
            if cell == ".":
                continue
            if cell in rows[r] or cell in cols[c] or cell in squares[square]:
                return False
            rows[r].add(cell)
            cols[c].add(cell)
            squares[square].add(cell)

    return True
```

**Time complexity**  
Technically $O(1)$ the board size is always 9x9.  
However, if the board has size $n \times n$, then the time complexity becomes $O(n^2)$ since we have to loop through each cell.

**Space complexity**  
Technically $O(1)$ for the same reasons above.  
However, if the board has size $n \times n$, the space complexity becomes $O(n \times n)$ because we create 3 hashmaps where the values are sets that have to hold, worst-case, $n$ numbers.
