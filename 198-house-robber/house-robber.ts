function rob(nums: number[]): number {
    if (nums.length === 0) return 0;
    if (nums.length === 1) return nums[0];
    
    // dp[i] represents the maximum amount that can be robbed up to house i
    const dp: number[] = new Array(nums.length);
    
    // Base cases
    dp[0] = nums[0];                    // Only first house available
    dp[1] = Math.max(nums[0], nums[1]); // Max of first or second house
    
    // For each house i, we can either:
    // 1. Rob house i and add it to amount from i-2
    // 2. Skip house i and keep amount from i-1
    for (let i = 2; i < nums.length; i++) {
        dp[i] = Math.max(dp[i-2] + nums[i], dp[i-1]);
    }
    
    return dp[nums.length - 1];
};