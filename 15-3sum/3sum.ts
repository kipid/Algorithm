function threeSum(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);
    const n = nums.length;
    const res = [];
    const added = new Set<string>();
    if (nums[0] > 0 || nums[n - 1] < 0) return res;
    for (let i = 0; i < n - 2; i++) {
        if (i > 0 && nums[i] === nums[i-1]) continue;

        let left = i + 1;
        let right = n - 1;

        while (left < right) {
            const sum = nums[i] + nums[left] + nums[right];
            if (sum === 0) {
                res.push([nums[i], nums[left], nums[right]]);

                while (left < right && nums[left] === nums[left+1]) left++;
                while (left < right && nums[right-1] === nums[right]) right--;

                left++;
                right--;
            }
            else if (sum < 0) {
                left++;
            }
            else {
                right--;
            }
        }
    }
    return res;
};