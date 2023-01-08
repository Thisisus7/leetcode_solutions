/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 var searchInsert = function(nums, target) {
    let l = 0;
    let r = nums.length - 1;

    while (l <= r) {
        mid = Math.floor(l + r);

        if (target == nums[mid]) return mid;
        if (target < nums[mid]) r = mid - 1;
        else l = mid + 1;
    }
    return l;
};

output1 = searchInsert(nums = [1,3,5,6], target = 5);
output2 = searchInsert(nums = [1,3,5,6], target = 2);
output3 = searchInsert(nums = [1,3,5,6], target = 7);
console.log(output1, output2, output3);