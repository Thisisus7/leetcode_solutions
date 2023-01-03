/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const numSet = new Set(nums);
    let longest = 0;

    for (n of numSet) {
        if (!(numSet.has(n-1))) {
            let length = 0;

            while (numSet.has(n + length)) length++;

            longest = Math.max(length, longest);
        }
    }
    return longest;
};