# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def diff(root: Optional[TreeNode], min_val: int, max_val: int) -> int:
            if not root:
                return 0
            min_val = min(min_val, root.val)
            max_val = max(max_val, root.val)
            curr_diff = max(abs(min_val - root.val), abs(max_val - root.val))
            max_left = diff(root.left, min_val, max_val)
            max_right = diff(root.right, min_val, max_val)
            return max(curr_diff, max(max_left, max_right))
            
        return diff(root, root.val, root.val)