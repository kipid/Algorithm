class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word: str):
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        cur['isWord'] = True
    
    def remove(self, word: str) -> bool:
        cur = self.root
        stack = []
        for letter in word:
            if letter not in cur:
                return False
            stack.append((cur, letter))
            cur = cur[letter]
        res = 'isWord' in cur
        if res:
            del cur['isWord']
        while stack:
            if len(cur)==0:
                cur, letter = stack.pop()
                del cur[letter]
            else:
                break
        return res
    
    def search(self, word: str) -> bool:
        cur = self.root
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]
        return 'isWord' in cur

    def startsWith(self, word: str) -> dict:
        cur = self.root
        for letter in word:
            if letter not in cur:
                return False
            cur = cur[letter]
        return cur

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        m = len(board)
        n = len(board[0])
        boolBoard = [[True] * (n+2) for _ in range(m+2)]
        for j in range(n+2):
            boolBoard[m][j] = False
            boolBoard[-1][j] = False
        for i in range(m+2):
            boolBoard[i][n] = False
            boolBoard[i][-1] = False
        
        def boolCopy(boolBoard: List[List[bool]]) -> List[List[bool]]:
            boolBoardCopy = []
            for i in range(m+2):
                row = []
                for j in range(n+2):
                    row.append(boolBoard[i][j])
                boolBoardCopy.append(row)
            return boolBoardCopy
        
        res = set()
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def dfs(row, col, cur, str_, boolBoard):
            if cur:
                if 'isWord' in cur:
                    res.add(str_)
                    trie.remove(str_)
                for dr, dc in moves:
                    r, c = row+dr, col+dc
                    if boolBoard[r][c]:
                        if board[r][c] in cur:
                            boolBoard[r][c] = False
                            dfs(r, c, cur[board[r][c]], str_ + board[r][c], boolCopy(boolBoard))
                            boolBoard[r][c] = True
                cur = False
        
        for i in range(m):
            for j in range(n):
                boolBoardCopy = boolCopy(boolBoard)
                row = i
                col = j
                str_ = board[row][col]
                if (cur := trie.startsWith(str_)):
                    boolBoardCopy[row][col] = False
                    dfs(row, col, cur, str_, boolBoardCopy)
        return res
