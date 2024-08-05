class Solution:
    def climbStairs(self, n: int) -> int:
        climbStairsSteps = [0, 1, 2]
        if n < 3:
            return climbStairsSteps[n]
        for i in range(3, n + 1):
            climbStairsSteps.append(climbStairsSteps[i - 1] + climbStairsSteps[i - 2])
        return climbStairsSteps[n]