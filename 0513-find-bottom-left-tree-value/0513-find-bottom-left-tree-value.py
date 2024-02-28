from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        q = deque([root])
        left_value = root.val
        
        while q:
            curr = q.popleft()
            left_value = curr.val
            if curr.right:
                q.append(curr.right)
            if curr.left:
                q.append(curr.left)
        return left_value