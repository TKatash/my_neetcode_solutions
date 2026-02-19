from collections import defaultdict

board = [
    ["1", "2", ".", ".", "3", ".", ".", ".", "."],
    ["4", ".", ".", "5", ".", ".", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", ".", "3"],
    ["5", ".", ".", ".", "6", ".", ".", ".", "4"],
    [".", ".", ".", "8", ".", "3", ".", ".", "5"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", ".", ".", ".", ".", ".", "2", ".", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "8"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]


def isValidSudoku(board):
    squares = defaultdict(set)
    rows = defaultdict(set)
    columns = defaultdict(set)
    for i in range(9):
        for j in range(9):
            cell = board[i][j]
            if cell != ".":
                if (
                    cell in rows[i]
                    or cell in columns[j]
                    or cell in squares[(i // 3, j // 3)]
                ):
                    return False
                rows[i].add(cell)
                columns[j].add(cell)
                squares[(i // 3, j // 3)].add(cell)
    return True


print(isValidSudoku(board))
