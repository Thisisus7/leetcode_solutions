/**
 * @param {number} n
 * @return {number}
 */
var getMaximumGenerated = function(n) {
    if (n == 0) return 0;

    let nums = [0, 1];
    for (let i=2; i<n+1; i++) {
        if (i % 2 == 0) nums.push(nums[Math.round(i/2)])
        else nums.push(nums[Math.round((i-1) / 2)] + nums[Math.round((i-1) / 2 + 1)])
    }
    return nums.reduce((a, b) => Math.max(a, b), -Infinity);  // Returns -Infinity if no parameters are provided.
};

var getMaximumGenerated = function(n) {
    if (n == 0) return 0;

    const nums = [0, 1];
    let res = 1;
    for (let i=2; i<n+1; i++) {
        if (i % 2 == 0) nums.push(nums[Math.round(i/2)])
        else nums.push(nums[Math.round((i-1) / 2)] + nums[Math.round((i-1) / 2 + 1)])

        res = Math.max(res, nums[i]);
    }
    return res; 
};