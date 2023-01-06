/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
 var maxResult = function(nums, k) {
    const dp = new Array(nums.length);
    dp[0] = nums[0];
    let window = [0];

    for (let i=1; i<nums.length; i++) {
        if (window[0] == i - (k+1)) {
            window.shift();
        }
        dp[i] = dp[window[0]] + nums[i];

        while (window.length && dp[window[window.length - 1]] <= dp[i]) {
            window.pop();
        }
        window.push(i);
    }
    return dp.pop();
};

output1 = maxResult([1,-1,-2,4,-7,3], 2); 
output2 = maxResult([10,-5,-2,4,0,3], 3); 
output3 = maxResult([1,-5,-20,4,-1,3,-6,-3], 2); 
console.log(output1, output2, output3);