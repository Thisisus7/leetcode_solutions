/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var containsNearbyDuplicate = function(nums, k) {
    const hash = new Map();

    for (let i=0; i<nums.length; i++) {
        if (nums[i] in hash && Math.abs(i - hash[nums[i]]) <= k) return true;

        hash[nums[i]] = i;
    }
    return false;
};
var containsNearbyDuplicate = function(nums, k) {
    const hash = new Set();

    for (let i=0; i<nums.length; i++) {
        if (i > k) hash.delete(nums[i-k-1]);
        if (hash.has(nums[i])) return true;

        hash.add(nums[i]);
    }
    return false;
};