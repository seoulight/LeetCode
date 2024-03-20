# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node = list1
        i = 0
        while node and i <= b:
            if i == a - 1:
                temp = node.next
                node.next = list2
                node = temp
            else:
                node = node.next
            i += 1
        node2 = list2
        while node2 and node2.next:
            node2 = node2.next
        node2.next = node
        return list1
                
            