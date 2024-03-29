/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    let l = 0, r = nums.length - 1;

    while (l <= r) {
        mid = Math.floor((l + r) / 2);
        if (nums[mid] == target) return mid;

        // mid in left portion
        if (nums[l] <= nums[mid]) {
            if (target < nums[mid] && target >= nums[l]) r = mid - 1;
            else l = mid + 1;
        }
        // mid in right portion
        else {
            if (target > nums[mid] && target <= nums[r]) l = mid + 1;
            else r = mid - 1;
        }
    }
    return -1;
};