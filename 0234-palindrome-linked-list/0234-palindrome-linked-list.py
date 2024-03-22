# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        palindrome = ""
        while head:
            palindrome += str(head.val)
            head = head.next
        n = len(palindrome)
        for i in range((n // 2) + 1):
            if palindrome[i] != palindrome[n - i - 1]:
                return False
        return True
            
        