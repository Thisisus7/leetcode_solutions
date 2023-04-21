/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} headA
 * @param {ListNode} headB
 * @return {ListNode}
 */
var getIntersectionNode = function(headA, headB) {
    let ptr1 = headA, ptr2 = headB;

    while (ptr1 != ptr2) {
        ptr1 ? ptr1 = ptr1.next : ptr1 = headB;
        ptr2 ? ptr2 = ptr2.next : ptr2 = headA;
    }
    return ptr1;
};