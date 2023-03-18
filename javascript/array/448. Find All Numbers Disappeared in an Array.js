/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    const numsSet = new Set(nums);
    const range = new Set(Array.from({length: nums.length}, (_, i) => i + 1));
    const res = [...range].filter(num => !numsSet.has(num));
    return res;
};

var findDisappearedNumbers = function(nums) {
    for (let n of nums) {
        i = Math.abs(n) - 1;
        nums[i] = -1 * Math.abs(nums[i]);
    }
    const res = [];
    for (const [i, n] of nums.entries()) {
        if (n > 0) res.push(i + 1);
    }
    return res;
}