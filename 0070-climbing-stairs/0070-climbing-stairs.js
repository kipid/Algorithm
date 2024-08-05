/**
 * @param {number} n
 * @return {number}
 */
const climbStairsSteps = [0, 1, 2]
const climbStairs = function(n) {
    if (climbStairsSteps[n]) {
        return climbStairsSteps[n];
    }
    else {
        for (let i = 3; i <= n; i++) {
            climbStairsSteps[i] = climbStairsSteps[i-1] + climbStairsSteps[i-2];
        }
        return climbStairsSteps[n];
    }
};