/**
 * @param {number[]} nums
 * @return {number}
 */
var maxSubArray = function(nums) {
    let maxSub = nums[0];
    let curSum = 0;

    for (n of nums) {
        if (curSum < 0) curSum = 0;

        curSum += n;
        maxSub = Math.max(curSum, maxSub);
    }
    return maxSub;
};