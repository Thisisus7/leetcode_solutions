/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
 var coinChange = function(coins, amount) {
    const dp = new Array(amount + 1).fill(amount+1);
    dp[0] = 0;

    for (let a=1; a<dp.length; a++) {
        for (c of coins) {
            if (a - c >= 0) {
                dp[a] = Math.min(dp[a], 1 + dp[a - c]);
            }
        }
    }
    return dp[amount] != amount+1 ? dp[amount] : -1;
};

output1 = coinChange([1,2,5], 11);
output2 = coinChange([2], 3);
output3 = coinChange([1], 0);
console.log(output1, output2, output3);