function numDecodings(s: string): number {
    if (!s || s[0] === '0') return 0;
    
    const n = s.length;
    // dp[i] represents number of ways to decode string up to index i
    const dp = new Array(n + 1).fill(0);
    
    // Empty string has 1 way to decode
    dp[0] = 1;
    // First character has 1 way if not '0'
    dp[1] = 1;
    
    for (let i = 2; i <= n; i++) {
        // Check single digit
        if (s[i - 1] !== '0') {
            dp[i] += dp[i - 1];
        }
        
        // Check two digits
        const twoDigit = parseInt(s.substring(i - 2, i));
        if (twoDigit >= 10 && twoDigit <= 26) {
            dp[i] += dp[i - 2];
        }
    }
    
    return dp[n];
};