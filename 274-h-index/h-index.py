class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        maxC = max(citations);
        cCount = [0] * (maxC + 2)
        for c in citations:
            cCount[c] += 1
        for i in range(maxC, -1, -1):
            cCount[i] += cCount[i+1]
            if cCount[i] >= i:
                return i
        