function rob(nums: number[]): number {
    if (nums.length === 0) { return 0; }
    if (nums.length === 1) { return nums[0]; }
    if (nums.length === 2) { return Math.max(nums[0], nums[1]); }

    const robLinear = (nums0: number[]): number => {
        let prev = 0;
        let curr = 0;
        for (let money of nums0) {
            const temp = curr;
            curr = Math.max(prev + money, curr);
            prev = temp;
        }
        return curr;
    }
    const moneyWithoutLast = robLinear(nums.slice(0, -1));
    const moneyWithoutFirst = robLinear(nums.slice(1));
    return Math.max(moneyWithoutLast, moneyWithoutFirst);
};