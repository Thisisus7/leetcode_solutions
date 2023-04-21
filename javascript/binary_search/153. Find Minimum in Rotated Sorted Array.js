/**
 * @param {number[]} nums
 * @return {number}
 */

// method 1
var findMin = function(nums) {
    let l = 0, r = nums.length - 1;
    res = nums[0];

    while (l <= r) {
        if (nums[l] < nums[r]) {
            res = Math.min(res, nums[l]);
            break;
        }
        m = (l + r) >> 1;
        res = Math.min(res, nums[m]);
        if (nums[m] > nums[r]) l = m + 1;
        else r = m - 1;
    }
    return res;
};

// method 2
var findMin = function(nums) {
    let l = 0, r = nums.length - 1;

    while (l < r) {
        m = (l + r) >> 1;
        if (nums[m] > nums[r]) l = m + 1;
        else r = m;
    }
    return nums[r];
};