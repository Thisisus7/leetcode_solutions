/**
 * @param {number[]} nums
 * @return {number}
 */
var maxProduct = function(nums) {
    let res = nums.reduce((a, b) => Math.max(a, b), -Infinity);
    let curMax = 1, curMin = 1;

    for (let n of nums) {
        temp = curMax * n;
        curMax = Math.max(curMax * n, curMin * n, n)
        curMin = Math.min(temp, curMin * n, n);
        res = Math.max(curMax, res);
    }
    return res;
};