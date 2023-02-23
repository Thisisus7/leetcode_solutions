/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
// Two pointer I
var isPalindrome = function(head) {
    const nums = [];

    while (head) {
        nums.push(head.val);
        head = head.next;
    }
    let l = 0, r = nums.length - 1;
    while (l <= r) {
        if (nums[l] != nums[r]) return false;

        l++;
        r--;
    }
    return true;
};
// Two pointer I
var isPalindrome = function(head) {
    let fast = head, slow = head;

    // mid
    while (fast && fast.next) {
        fast = fast.next.next;
        slow = slow.next;
    };
    // reverse
    let prev = null;
    while (slow) {
        let temp = slow.next;
        slow.next = prev;
        prev = slow;
        slow = temp;
    };
    // check
    let l = head, r = prev;
    while (r) {
        if (l.val != r.val) return false;

        l = l.next;
        r = r.next;
    };
    return true;
};