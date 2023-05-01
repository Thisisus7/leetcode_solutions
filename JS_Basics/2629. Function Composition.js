// Nested function: loop; reduce()

/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
	return function(x) {
        // Method 1
        // for (let i=functions.length-1; i>=0; i--) x = functions[i](x);
        // return x;

        // Method 2
        // return functions.reduceRight((acc, cur) => {
        //     return cur(acc);
        // }, x);

        // Method 3
        return functions.reduceRight((acc, cur) => cur(acc), x);
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */