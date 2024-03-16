import copy

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        boolMap = [[True] * (n+2) for _ in range(m+2)]
        for col in range(n+2):
            boolMap[-1][col] = False
            boolMap[m][col] = False
        for row in range(m+2):
            boolMap[row][-1] = False
            boolMap[row][n] = False
        moves = [[0,1], [1,0], [0,-1], [-1,0]]

        def startSearch(row: int, col: int, length: int, boolMapCopy: List[List[bool]]) -> bool:
            if length == len(word):
                return True
            if boolMapCopy[row][col]:
                boolMapCopy[row][col] = False
                matched = False
                for move in moves:
                    if boolMapCopy[row+move[0]][col+move[1]] and word[length] == board[row+move[0]][col+move[1]]:
                        matched = matched or startSearch(row+move[0], col+move[1], length+1, copy.deepcopy(boolMapCopy))
                return matched
            else:
                return False

        res = False
        wordDict = dict()
        for char in word:
            wordDict[char] = wordDict.get(char, 0) + 1
        for row in range(m):
            for col in range(n):
                if board[row][col] in wordDict:
                    wordDict[board[row][col]] -= 1
                    if wordDict[board[row][col]] == 0:
                        del wordDict[board[row][col]]
        if len(wordDict) != 0:
            return False
        firstChar = word[0]
        sameFirstCharLength = 1
        for i in range(1, len(word)):
            if word[i] != firstChar:
                break
            sameFirstCharLength += 1
        lastChar = word[-1]
        sameLastCharLength = 1
        for i in range(len(word)-2, -1, -1):
            if word[i] != lastChar:
                break
            sameLastCharLength += 1
        if sameFirstCharLength > sameLastCharLength:
            word = word[::-1]
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    res = res or startSearch(row, col, 1, copy.deepcopy(boolMap))
        return res