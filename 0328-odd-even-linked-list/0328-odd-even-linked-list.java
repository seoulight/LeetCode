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
    public ListNode oddEvenList(ListNode head) {
        ListNode last = head, node = head;
        int size = 1;
        
        if (head == null) {
            return head;
        }
        while (last.next != null) {
            last = last.next;
            size++;
        }
        size /= 2;
        while (node.next != null && --size >= 0) {
            last.next = node.next;
            last = last.next;
            node.next = node.next.next;
            node = node.next;
            last.next = null;
        }
        return head;
    }
}