/**
 * @param {number[]} gas
 * @param {number[]} cost
 * @return {number}
 */
var canCompleteCircuit = function(gas, cost) {
    const sumGas = gas.reduce((acc, val) => acc + val);
    const sumCost = cost.reduce((acc, val) => acc + val);
    if (sumGas < sumCost) return -1;

    let res = 0, total = 0;
    for (let i=0; i<gas.length; i++) {
        total += gas[i] - cost[i];

        if (total < 0) {
            res = i + 1;
            total = 0;
        }
    }
    return res;
}; 

// more suitable for javascript
var canCompleteCircuit = function(gas, cost) {
    let res = 0, curSum = 0, sum = 0;

    for (let i=0; i<gas.length; i++) {
        curSum += gas[i] - cost[i];
        sum += gas[i] - cost[i];
        if (curSum < 0) {
            res = i + 1;
            curSum = 0;
        }
    }
    if (sum < 0) return -1;

    return res;
}; 