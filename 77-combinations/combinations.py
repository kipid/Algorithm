class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # n, n-1, n-2, ..., n-k+1
        res = []

        def ithCombine(i: int, maxN: int, path: List[int]):
            if i == 0:
                res.append(path)
                return
            for j in range(maxN+1, n-i+2):
                ithCombine(i-1, j, path + [j])
        
        ithCombine(k, 0, [])
        return res