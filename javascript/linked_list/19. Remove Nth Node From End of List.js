/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */

// own
var removeNthFromEnd = function(head, n) {
    if (!head.next) return null;

    let l = null, r = head;
    while (r) {
        const nxt = r.next;
        r.next = l;
        l = r;
        r = nxt;
    }

    let cnt = 1;
    while (l) {
        const nxt = l.next;
        if (n != cnt) {
            l.next = r;
            r = l;
        }
        l = nxt;
        cnt += 1;
    }
    return r;
};

// No need to reverse
var removeNthFromEnd = function(head, n) {
    const dummy = new ListNode(0, head);
    let l = dummy, r = head;

    while (n > 0 && r) {
        r = r.next;
        n --;
    }

    while (r) l = l.next, r = r.next;

    l.next = l.next.next;
    return dummy.next;
};