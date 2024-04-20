class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        flatBoard = []
        lastN = n**2
        for i in range(n):
            if (n-i)%2 == 1:
                for j, move in enumerate(board[i][::-1]):
                    flatBoard.append((lastN-n*i-j, move))
            else:
                for j, move in enumerate(board[i]):
                    flatBoard.append((lastN-n*i-j, move))
        flatBoard.reverse()
        print(f"{flatBoard = }")
        visited = set([(1,-1)])
        q = deque([(1,0)])
        while q:
            curr, count = q.popleft()
            if curr >= lastN:
                return count
            for move in range(curr + 1, min(curr + 7, lastN + 1)):
                curr = move
                if flatBoard[curr-1][1] != -1:
                    curr = flatBoard[curr-1][1]
                if flatBoard[curr-1] not in visited:
                    visited.add(flatBoard[curr-1])
                    q.append((curr, count + 1))
        return -1