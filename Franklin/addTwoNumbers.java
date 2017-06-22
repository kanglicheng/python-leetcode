/*
lc problem 2
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
*/

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    // My solution
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry=0;
        int p = l1.val;
        int q = l2.val;
        int sum = p+q+carry;
        carry = sum/10; sum = sum%10;
        ListNode ln = new ListNode(sum);
        ListNode result = ln;
        l1 = l1.next; l2 = l2.next;
        while (l1!=null || l2!=null) {
            p = l1!=null?l1.val:0; l1 = l1!=null?l1.next:null;
            q = l2!=null?l2.val:0; l2 = l2!=null?l2.next:null;
            sum = p+q+carry;
            carry = sum/10; sum = sum%10;
            ln.next = new ListNode(sum); ln = ln.next;
        }
        if (carry>0) {
            ln.next = new ListNode(1); ln = ln.next;
        }
        return result;
    }

    // Editorial solution
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode dummyHead = new ListNode(0);
        ListNode p = l1, q = l2, curr = dummyHead;
        int carry = 0;
        while (p != null || q != null) {
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            int sum = carry + x + y;
            carry = sum / 10;
            curr.next = new ListNode(sum % 10);
            curr = curr.next;
            if (p != null) p = p.next;
            if (q != null) q = q.next;
        }
        if (carry > 0) {
            curr.next = new ListNode(carry);
        }
        return dummyHead.next;
    }

    // instead of doing an extra operation before the start of while loop,
    // the editorial soln just used a dummyHead var and return dummyHead.next at the end.
    // Pretty elegant!
}