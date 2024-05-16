class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        neighbors = [(-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1), (-1,0)]

        def liveNeighbors(i: int, j: int) -> int:
            lives = 0
            for dx, dy in neighbors:
                x = i+dx
                y = j+dy
                if 0 <= x < m and 0 <= y < n:
                    # print(f"{x = }, {y = }, {board[x][y] = }")
                    lives += board[x][y]%2
            return lives
        
        for r in range(m):
            for c in range(n):
                liveN = liveNeighbors(r, c)
                # print(f"{r = }, {c = }, {liveN = }")
                if board[r][c] == 0:
                    if liveN == 3:
                        board[r][c] += 2
                else:
                    if liveN == 2 or liveN == 3:
                        board[r][c] += 2
        for r in range(m):
            for c in range(n):
                if board[r][c] > 1:
                    board[r][c] = 1
                else:
                    board[r][c] = 0
        