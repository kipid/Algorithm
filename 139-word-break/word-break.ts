function wordBreak(s: string, wordDict: string[]): boolean {
    // Convert wordDict to Set for O(1) lookup
    const wordSet = new Set(wordDict);
    const n = s.length;
    
    // dp[i] represents if s[0...i-1] can be segmented
    const dp = new Array(n + 1).fill(false);
    dp[0] = true;  // Empty string is valid
    
    // For each ending position
    for (let i = 1; i <= n; i++) {
        // Try all possible starting positions
        for (let j = 0; j < i; j++) {
            // If prefix is valid and substring is in dictionary
            if (dp[j] && wordSet.has(s.substring(j, i))) {
                dp[i] = true;
                break;  // No need to check further starting positions
            }
        }
    }
    
    return dp[n];
};