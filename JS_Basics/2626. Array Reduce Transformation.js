// Simulate .reduce()

/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    // return nums.reduce((accum, curr) => {
    //     return fn(accum, curr);
    // }, init);
    nums.forEach((x) => {
        init = fn(init, x);
    });
    return init;
};

// Input: 
// nums = [1,2,3,4]
// fn = function sum(accum, curr) { return accum + curr * curr; }
// init = 100
// Output: 130