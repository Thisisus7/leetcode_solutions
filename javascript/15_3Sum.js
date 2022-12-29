/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    const res = [];
    nums.sort((num1, num2) => num1 - num2);  // sort() will cause error when sorting negative numbers

    for (let i = 0; i < nums.length; i++) {
        if (i > 0 && nums[i] == nums[i-1]) continue;
        let l = i + 1, r = nums.length - 1;
        while (l < r){          
            if (nums[i] + nums[l] + nums[r] == 0) {
                res.push([nums[i], nums[l], nums[r]]);
                l++;
                while (l < r && nums[l] == nums[l - 1]) l++;
            } 
            else {
                nums[i] + nums[l] + nums[r] > 0 ? r-- : l++;
            }
        }
    }
    return res;
};