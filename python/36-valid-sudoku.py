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
