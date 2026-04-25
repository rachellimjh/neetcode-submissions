class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        row = defaultdict(list)
        column = defaultdict(list)
        square = defaultdict(list)

        for i in range(n):
            for j in range (n):
                if board[i][j] == '.':
                    continue
                # Check row, column, and box (square)
                if board[i][j] in row[i] or board[i][j] in column[j] or board[i][j] in square[(i // 3, j // 3)]:
                    return False

                # Add to row, column, and box
                row[i].append(board[i][j])
                column[j].append(board[i][j])
                square[(i // 3, j // 3)].append(board[i][j])
        return True