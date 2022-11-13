/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
// 1.Loop
var twoSum = function(nums, target) {
    for (let i=0; i<nums.length; i++) {
        for (let j=i+1; j<nums.length; j++) {
            if (nums[i] + nums[j] == target) {
                return [i, j];
            }
        }
    }
};

// 2. Hashmap
var twoSum2 = function(nums, target) {
    const map = new Map();  // create a map (a collection of key-value pairs)
    for(let i=0; i<nums.length; i++) {
        const complement = target - nums[i];
        if(map.has(complement)) {
            return [map.get(complement), i];
        }
        map.set(nums[i], i);  // key: nums[i], value: i
    }
    return [];
};