/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */

/**
 * 
 * @param {ListNode} list1 
 * @param {ListNode} list2
 * @return {ListNode} 
 */

// 1. Iteration
var mergeTwoLists = function(list1, list2) {
    const prehead = new ListNode(-1);
    let temp = prehead;

    while (list1 && list2) {
        if (list1.val < list2.val) {
            temp.next = list1;
            list1 = list1.next;
        }
        else {
            temp.next = list2;
            list2 = list2.next;
        }
        temp = temp.next;
    }
    temp.next = list1 === null ? list2 : list1;

    return prehead.next;
};

// 2. Recursion
var mergeTwoLists = function(list1, list2) {
    if (!list1) return list2;
    else if (!list2) return list1;
    else if (list1.val < list2.val) {
        list1.next = mergeTwoLists(list1.next, list2);
        return list1;
    }
    else {
        list2.next = mergeTwoLists(list1, list2.next);
        return list2;
    }
}