/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        ListNode node = head;
        int length = 0;
        while (node != null) {
            node = node.next;
            length++;
        }
        node = head;
        if (length == n) {
            return head.next;
        }
        n = length - n;
        while (node != null && n > 0) {
            if (n == 1) {
                node.next = node.next.next;
            }
            node = node.next;
            n--;
        }
        return head;
        
    }
}