const steps = [1, 1, 2];

function climbStairs(n: number): number {
    if (steps[n]) {
        return steps[n];
    }
    steps[n] = climbStairs(n-1) + climbStairs(n-2);
    return steps[n];
};