class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        row = defaultdict(list)  # Use defaultdict for lists
        col = defaultdict(list)
        square = defaultdict(list)  # For 3x3 squares

        for i in range(n):
            for j in range(n):
                if board[i][j]=='.':
                    continue
                if (board[i][j] in row[i] or
                    board[i][j] in col[j] or
                    board[i][j] in square[i//3,j//3]):
                    return False
                else:
                    row[i].append(board[i][j])
                    col[j].append(board[i][j])
                    square[i//3,j//3].append(board[i][j])
        return True