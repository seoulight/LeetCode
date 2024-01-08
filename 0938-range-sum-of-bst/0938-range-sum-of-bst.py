# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0
        def visit(node: Optional[TreeNode]):
            if not node:
                return
            if low <= node.val <= high:
                nonlocal answer
                answer += node.val
            if low == node.val:
                visit(node.right)
            elif high == node.val:
                visit(node.left)
            else:
                visit(node.left)
                visit(node.right)
        visit(root)
        return answer