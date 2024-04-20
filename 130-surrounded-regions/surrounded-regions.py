class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        
        def capture(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != "O":
                return
            board[r][c] = "T"  # Temporarily mark as 'T'
            # Recursively capture adjacent cells
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)
        
        # Capture all 'O' regions connected to the border
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and (r == 0 or r == rows - 1 or c == 0 or c == cols - 1)):
                    capture(r, c)
        
        # Flip remaining 'O' cells to 'X'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"  # Convert 'O' to 'X'
        
        # Convert 'T' cells back to 'O'
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"  # Convert back from 'T' to 'O'
