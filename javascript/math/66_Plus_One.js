/**
 * @param {number[]} digits
 * @return {number[]}
 */
 var plusOne = function(digits) {
    digits = digits.reverse();
    let i = 0;
    let one = 1;

    while (one) {
        if (i < digits.length) {
            if (digits[i] == 9) {
                digits[i] = 0;
            }
            else {
                digits[i]++;
                one = 0;
            }
        }
        else {
            digits.push(1);
            one = 0;
        }
        i++;
    }
    return digits.reverse();
};

output1 = plusOne([1, 2, 3]);
output2 = plusOne([4, 3, 2, 1]);
output3 = plusOne([9]);
console.log(output1, output2, output3);