/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersection = function(nums1, nums2) {
    const set1 = new Set(nums1);
    const res = [];

    for (n of nums2) {
        if (set1.has(n)) {
            res.push(n);
            set1.delete(n);
        }
    }
    return res;
};

// a more elegant way
var intersection = function(nums1, nums2) {
    const set1 = new Set(nums1)
    return [...new Set(nums2)].filter((val) => set1.has(val))
};