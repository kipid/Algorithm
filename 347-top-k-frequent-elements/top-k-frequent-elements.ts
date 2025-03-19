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
    console.log(arrays);
    arrays.sort((a, b) => b[1] - a[1]);
    const res = [];
    for (let i = 0; i < k; i++) {
        res.push(arrays[i][0]);
    }
    return res;
};