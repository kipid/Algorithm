/**
 * @param {number} n
 * @return {number}
 */
const climbStairsRes = [0, 1, 2];
function climbStairs(n) {
    if (climbStairsRes[n]) {
        return climbStairsRes[n];
    }
    for (let i = 3; i <= n; i++) {
        climbStairsRes[i] = climbStairs(i-1) + climbStairs(i-2);
    }
    return climbStairsRes[n];
};