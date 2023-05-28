// Closure: 3 ways

/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let count = init;
    // function declaration
    function increment() {
        return ++count;
    }
    // function expression
    const decrement = function() {
        return --count;
    }
    return {
        increment,
        decrement,
        reset: () => count = init, // arrow function
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */