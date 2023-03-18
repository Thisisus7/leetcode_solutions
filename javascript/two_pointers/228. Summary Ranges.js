/**
 * @param {number[]} nums
 * @return {string[]}
 */
var summaryRanges = function(nums) {
    if (nums.length === 0) return [];
    
    res = [];
    let l = 0, r = 0;
    while (r < nums.length) {
        if (r < nums.length-1 && nums[r]+1 == nums[r+1]) {
            r++;
        } else {
            nums[l] == nums[r] ? res.push("" + nums[l]) : res.push("" + nums[l] + "->" + nums[r]);
            l = r + 1;
            r++;
        }
    }
    return res;
};