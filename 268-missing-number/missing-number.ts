function missingNumber(nums: number[]): number {
    const dict = {};
    for (let i = 0; i <= nums.length; i++) {
        dict[`key${i}`] = i;
    }
    for (let num of nums) {
        delete dict[`key${num}`];
    }
    return dict[Object.keys(dict)[0]]
};