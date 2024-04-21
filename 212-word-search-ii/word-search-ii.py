class Trie:
    def __init__(self):
        self.root = {}
    
    def insert(self, word: str):
        cur = self.root
        for letter in word:
            if letter not in cur:
                cur[letter] = {}
            cur = cur[letter]
        cur['isWord'] = word
    
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

        res = set()
        moves = [(0,1), (1,0), (0,-1), (-1,0)]
        
        def dfs(row, col, cur):
            letter = board[row][col]
            board[row][col] = ""
            if letter in cur:
                cur = cur[letter]
                if 'isWord' in cur:
                    res.add(cur['isWord'])
                    trie.remove(cur['isWord'])
                if row > 0:
                    dfs(row-1, col, cur)
                if row < m-1:
                    dfs(row+1, col, cur)
                if col > 0:
                    dfs(row, col-1, cur)
                if col < n-1:
                    dfs(row, col+1, cur)
            board[row][col] = letter

        for i in range(m):
            for j in range(n):
                dfs(i, j, trie.root)
                    
        return res
