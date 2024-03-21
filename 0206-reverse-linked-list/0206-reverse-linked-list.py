# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev_node = None
        while node:
            temp = node.next
            node.next = prev_node
            if not temp:
                return node
            prev_node = node
            node = temp
        return node