function canJump(nums: number[]): boolean {
    let maxReach = 0;  // Tracks the furthest index we can reach
    
    // Iterate through the array
    for (let i = 0; i < nums.length; i++) {
        // If we can't reach the current position, return false
        if (i > maxReach) {
            return false;
        }
        
        // Update the maximum reachable position
        maxReach = Math.max(maxReach, i + nums[i]);
        
        // If we can already reach the last index, return true
        if (maxReach >= nums.length - 1) {
            return true;
        }
    }
    
    return true;  // If we complete the loop, we can reach the end
};