function twoSum(nums: number[], target: number): number[] {
    const n = nums.length;
    const map = new Map<number, number>();
    for (let i = 0; i < n; i++) {
        map.set(nums[i], i);
    }
    for (let i = 0; i < n-1; i++) {
        const anotherNum = target - nums[i];
        if (map.has(anotherNum)) {
            if (i !== map.get(anotherNum)) {
                return [i, map.get(anotherNum)];
            }
        }
    }
};