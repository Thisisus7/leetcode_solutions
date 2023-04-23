/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function(stones) {
    const maxHeap = new MaxPriorityQueue();
     // null: a placeholder for the actual value; stone: the priority value
    for (let stone of stones)  maxHeap.enqueue(null, stone); 

    while (maxHeap.size() > 1) {
        // dequeue() returns an object: {priority: <priority_value>, value: <actual_value>}
        const first = maxHeap.dequeue()['priority'];
        const second = maxHeap.dequeue()['priority'];
        if (first > second) maxHeap.enqueue(null, first - second);
    }
    return maxHeap.isEmpty() ? 0 : maxHeap.dequeue()['priority'];   
};