/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let l = 0;
    let r = 1;
    let maxProfit = 0;

    while (r < prices.length) {
        if (prices[l] < prices[r]) {
            profit = prices[r] - prices[l];
            maxProfit = Math.max(profit, maxProfit);
        }
        else l = r;
        r ++;
    }
    return maxProfit;
};

output1 = maxProfit(prices = [7,1,5,3,6,4])  // 5
output2 = maxProfit(prices = [7,6,4,3,1])  // 0
console.log(output1, output2)