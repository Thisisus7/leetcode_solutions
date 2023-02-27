/**
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var moveZeroes = function(nums) {
    let l = 0;

    for (let r=0; r<nums.length-1; r++) {
        if (nums[r]) {
            let temp = nums[r];
            nums[r] = nums[l];
            nums[l] = temp;
            l++;
        }
    }
};