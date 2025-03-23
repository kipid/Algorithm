function maxProduct(nums: number[]): number {
    if (nums.length === 0) return 0;
    
    // Track both max and min products ending at current position
    let maxSoFar = nums[0];
    let minSoFar = nums[0];
    let result = maxSoFar;
    
    // Start from second element
    for (let i = 1; i < nums.length; i++) {
        const curr = nums[i];
        // Store temp max because we'll need old max for min calculation
        const tempMax = Math.max(curr, maxSoFar * curr, minSoFar * curr);
        minSoFar = Math.min(curr, maxSoFar * curr, minSoFar * curr);
        maxSoFar = tempMax;
        
        // Update global maximum
        result = Math.max(result, maxSoFar);
    }
    
    return result;
};