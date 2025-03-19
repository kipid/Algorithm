function topKFrequent(nums: number[], k: number): number[] {
    const counts = new Map<number, number>();
    const n = nums.length;
    for (let i = 0; i < n; i++) {
        if (counts.has(nums[i])) {
            counts.set(nums[i], counts.get(nums[i])+1);
        }
        else {
            counts.set(nums[i], 1);
        }
    }
    const arrays = Array.from(counts.entries());
    arrays.sort((a, b) => b[1] - a[1]);
    return arrays.slice(0, k).map(([num]) => num);
};
