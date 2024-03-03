class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rCheck = [set() for _ in range(9)]
        cCheck = [set() for _ in range(9)]
        sCheck = [set() for _ in range(9)]
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] in rCheck[i]:
                        return False
                    else:
                        rCheck[i].add(board[i][j])
                    if board[i][j] in cCheck[j]:
                        return False
                    else:
                        cCheck[j].add(board[i][j])
                    s = i // 3 * 3 + j // 3
                    if board[i][j] in sCheck[s]:
                        return False
                    else:
                        sCheck[s].add(board[i][j])
        return True