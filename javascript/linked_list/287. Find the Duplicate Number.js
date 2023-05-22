/**
 * @param {number[]} nums
 * @return {number}
 */
var findDuplicate = function(nums) {
    let fast = 0, slow = 0, slow2 = 0;
    do {
        slow = nums[slow];
        fast = nums[nums[fast]];
    } while (fast !== slow);

    while (slow !== slow2) {
        slow = nums[slow];
        slow2 = nums[slow2];
    }
    return slow;
};