function maxArea(height: number[]): number {
    const n = height.length;
    let left = 0;
    let right = n-1;
    let max = Math.min(height[left], height[right]) * (right-left);
    if (height[left] < height[right]) {
        left++;
    } else {
        right--;
    }
    while (left < right) {
        max = Math.max(max, Math.min(height[left], height[right]) * (right-left));
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return max;
};