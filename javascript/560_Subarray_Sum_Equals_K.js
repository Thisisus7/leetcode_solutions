/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
 var subarraySum = function(nums, k) {
    let res = 0;
    let curSum = 0;
    const prefixSums = { 0 : 1 };

    for (let n of nums) {
        curSum += n;
        let diff = curSum - k;

        if (prefixSums[diff]) {
            res += prefixSums[diff];
        }
        if (prefixSums[curSum]) {
            prefixSums[curSum] ++;
        } else {
            prefixSums[curSum] = 1;
        }
    }
    return res;
};

output1 = subarraySum([1, 1, 1], 2);
output2 = subarraySum([1, 2, 3], 3);
console.log(output1, output2);