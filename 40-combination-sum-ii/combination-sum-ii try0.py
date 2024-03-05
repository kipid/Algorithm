class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        r = len(candidates) - 1
        res = []
        set_ = set()
        while r >= 0 and candidates[r] > target:
            r -= 1
        if r < 0:
            return res
        cutCandidates = []
        l0 = 0
        while l0 <= r:
            cand = candidates[l0]
            maxLength = target // cand
            k = l0
            while k <= r and k < l0 + maxLength and cand == candidates[k]:
                k += 1
            cutCandidates += candidates[l0:k]
            while k <= r and cand == candidates[k]:
                k += 1
            l0 = k

        print(cutCandidates)
        print(len(cutCandidates))
        r = len(cutCandidates) - 1
        
        def pathSum(left: int, path: list[int], sumUntil: int) -> bool:
            if sumUntil == target:
                if tuple(path) not in set_:
                    set_.add(tuple(path))
                    res.append(path)
                return True
            if sumUntil > target:
                return False
            while left+1 <= r and target >= sumUntil + cutCandidates[left+1]:
                pathSum(left+1, path + [cutCandidates[left+1]], sumUntil + cutCandidates[left+1])
                left += 1
                print(f"{left = }")
            return False

        for l in range(r+1):
            pathSum(l, [cutCandidates[l]], cutCandidates[l])
        return res

sol = Solution()
candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
target = 30
sol.combinationSum2(candidates, target)