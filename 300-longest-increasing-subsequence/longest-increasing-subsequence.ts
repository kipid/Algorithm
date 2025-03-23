function lengthOfLIS(nums: number[]): number {
    if (!nums.length) return 0;
    
    // tails[i] represents the smallest tail of all increasing subsequences of length i+1
    const tails: number[] = [];
    
    for (const num of nums) {
        // Find the position to insert num using binary search
        let left = 0;
        let right = tails.length;
        
        while (left < right) {
            const mid = Math.floor((left + right) / 2);
            if (tails[mid] < num) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        
        // If at end, extend the longest sequence
        if (left === tails.length) {
            tails.push(num);
        }
        // Otherwise replace the smallest number >= num
        else {
            tails[left] = num;
        }
    }
    
    return tails.length;
};