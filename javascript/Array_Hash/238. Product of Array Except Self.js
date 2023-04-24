/**
 * @param {number[]} nums
 * @return {number[]}
 */
var productExceptSelf = function(nums) {
    const res = new Array(nums.length).fill(1);

    let prefix = postfix = 1;
    let j = nums.length - 1;  // for postfix
    nums.forEach((val, i) => {
        // * prefix
        res[i] *= prefix;
        prefix *= val;
        // * postfix
        res[j] *= postfix;
        postfix *= nums[j];
        j--;
    });
    return res;
};