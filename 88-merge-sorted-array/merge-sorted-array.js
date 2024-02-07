/**
 * @param {number[]} nums1
 * @param {number} m
 * @param {number[]} nums2
 * @param {number} n
 * @return {void} Do not return anything, modify nums1 in-place instead.
 */
var merge = function(nums1, m, nums2, n) {
    for (let i = 0, j = 0; i < m + n; i++) {
        if (j < n) {
            if (i === m + j || nums1[i] > nums2[j]) {
                nums1.splice(i, 0, nums2[j]);
                nums1.splice(m + n, 1);
                j++;
            }
        }
    }
};