// Closure

/**
 * @return {Function}
 */
var createHelloWorld = function() {
    let res = "Hello World";
    return function(...args) {
        return res;
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */