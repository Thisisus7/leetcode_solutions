/**
 * @param {number} rowIndex
 * @return {number[]}
 */
var getRow = function(rowIndex) {
    let res = [1];

    for (let i=0; i<rowIndex; i++) {
        const temp = [0].concat(res, [0]);
        res = [];
        for (let j=0; j<temp.length-1; j++) {
            res.push(temp[j] + temp[j + 1]);
        }
    }
    return res;
};