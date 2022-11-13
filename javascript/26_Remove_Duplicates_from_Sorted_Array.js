/**
 * @param {number[]} nums
 * @return {number}
 */
 var removeDuplicates = function(nums) {
    l = 1;
    for (let r=1; r<nums.length; r++) {
        if (nums[r] != nums[r-1]) {
            nums[l] = nums[r];
            l ++;
        }
    }
    return l;
};

output1 = removeDuplicates([1, 1, 2]);
output2 = removeDuplicates([0,0,1,1,1,2,2,3,3,4]);
console.log(output1, output2)