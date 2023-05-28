/**
 * @param {number} k
 * @param {number[]} nums
 */
var KthLargest = function(k, nums) {
    this.queue = new MinPriorityQueue();
    this.k = k;
    nums.forEach((val) => {
        this.queue.enqueue(val);
    })
    while (this.queue.size() > this.k) this.queue.dequeue().element;
};

/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function(val) {
    this.queue.enqueue(val);
    if (this.queue.size() > this.k) this.queue.dequeue().element;

    return this.queue.front().element;
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */