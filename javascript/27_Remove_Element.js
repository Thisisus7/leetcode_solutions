/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
 var removeElement = function(nums, val) {
    let l = 0;

    for (let r=0; r<nums.length; r++) {
        if (nums[r] != val) {
            nums[l] = nums[r];
            l++;
        }
    }
    return l;
};

out1= removeElement(nums = [3,2,2,3], val = 3);
out2= removeElement(nums = [0,1,2,2,3,0,4,2], val = 2);
console.log(out1, out2);