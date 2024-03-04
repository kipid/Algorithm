class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        r = len(candidates) - 1
        while r >= 0 and candidates[r] > target:
            r -= 1
        if r < 0:
            return res

        def pathSum(left: int, path: List[int], sumUntil: int) -> bool:
            if sumUntil == target:
                res.append(path)
                return True
            elif sumUntil > target:
                return False
            while left <= r and target >= sumUntil + candidates[left]:
                pathSum(left, path + [candidates[left]], sumUntil + candidates[left])
                left += 1
            return False

        for l in range(r+1):
            pathSum(l, [candidates[l]], candidates[l])
        return res
