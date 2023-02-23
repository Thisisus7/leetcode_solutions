/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */
// Iteration
var removeElements = function(head, val) {
    const dummy = new ListNode(0);
    dummy.next = head;
    let prev = dummy;
    
    while (head) {
        if (head.val == val) prev.next = head.next;
        else prev = head;

        head = head.next;
    }
    return dummy.next;
};

// Recursion
var removeElements = function(head, val) {
    if (head === null) return head;

    head.next = removeElements(head.next, val);
    return head.val === val ? head.next : head;
};