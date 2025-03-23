function coinChange(coins: number[], amount: number): number {
    // dp[i] represents minimum coins needed for amount i
    const dp = new Array(amount + 1).fill(Infinity);
    
    // Base case: amount 0 needs 0 coins
    dp[0] = 0;
    
    // For each amount from 1 to target amount
    for (let i = 1; i <= amount; i++) {
        // Try each coin denomination
        for (const coin of coins) {
            if (i >= coin) {
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }
    
    // If dp[amount] is still Infinity, no solution exists
    return dp[amount] === Infinity ? -1 : dp[amount];
};