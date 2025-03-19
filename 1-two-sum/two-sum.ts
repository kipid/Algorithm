function twoSum(nums: number[], target: number): number[] {
    const n = nums.length;
    const map = new Map<number, number>();
    for (let i = 0; i < n; i++) {
        map.set(nums[i], i);
    }
    for (let i = 0; i < n-1; i++) {
        if (map.has(target - nums[i])) {
            if (i !== map.get(target - nums[i])) {
                return [i, map.get(target - nums[i])];
            }
        }
    }
};