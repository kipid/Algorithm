function combinationSum(candidates: number[], target: number): number[][] {
    const result: number[][] = [];
    
    // Helper function for backtracking
    function backtrack(start: number, target: number, current: number[]) {
        // Base case: if target becomes 0, we found a valid combination
        if (target === 0) {
            result.push([...current]);
            return;
        }
        
        // If target becomes negative, no need to continue this path
        if (target < 0) {
            return;
        }
        
        // Try each candidate from start index
        for (let i = start; i < candidates.length; i++) {
            // Add current candidate to combination
            current.push(candidates[i]);
            // Recursively try with same index (since we can reuse numbers)
            backtrack(i, target - candidates[i], current);
            // Backtrack by removing the last added number
            current.pop();
        }
    }
    
    // Start backtracking with empty combination
    backtrack(0, target, []);
    return result;
};