function topKFrequent(nums: number[], k: number): number[] {
    // Step 1: Count frequencies using Map
    const freqMap: Map<number, number> = new Map();
    for (const num of nums) {
        freqMap.set(num, (freqMap.get(num) || 0) + 1);
    }
    // Step 2: Convert to array of [number, frequency] pairs and sort
    const freqArray: [number, number][] = Array.from(freqMap.entries());
    freqArray.sort((a, b) => b[1] - a[1]); // Sort by frequency descending
    
    // Step 3: Take first k elements and extract numbers
    return freqArray.slice(0, k).map(([num]) => num);
};
