/**
 * @param {number[]} nums
 * @return {number}
 */
// DP
var lengthOfLIS = function(nums) {
    const LIS = new Array(nums.length).fill(1);
    for (let i=nums.length-1; i>=0; i--) {
        for (let j=i; j<nums.length; j++) {
            if (nums[i] < nums[j]) {
                LIS[i] = Math.max(LIS[i], 1 + LIS[j]);
            }
        }
    }
    return Math.max(...LIS);
};

// Greedy + Binary search
var lengthOfLIS = function(nums) {
    const LIS = [nums[0]];

    nums.forEach((num) => {
        if (num > LIS[LIS.length-1]) {
            LIS.push(num);
            return;
        }
        let l = 0, r = LIS.length - 1;
        while (l < r) {
            m = l + r >>> 1; 
            num > LIS[m] ? l = m + 1 : r = m;
        }
        LIS[r] = num; 
    })
    return LIS.length;
};