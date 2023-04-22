/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    const hashset = new Set();

    for (n of nums) {
        if (hashset.has(n)) return true;

        hashset.add(n);
    }
    return false;
};