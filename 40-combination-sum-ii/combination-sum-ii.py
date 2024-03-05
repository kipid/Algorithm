class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(i, comb, tot):
            if tot == target:
                ans.append(comb[:])
                return
            if i >= len(candidates) or tot > target:
                return
            for idx in range(i, len(candidates)):
                if idx > i and candidates[idx] == candidates[idx - 1]:
                    continue
                comb.append(candidates[idx])
                backtrack(idx + 1, comb, tot + candidates[idx])
                comb.pop()
        candidates.sort()
        backtrack(0, [], 0)
        return ans
