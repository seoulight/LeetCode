# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode], leaves: list):
            if not root:
                return 
            if not root.left and not root.right:
                leaves.append(root.val)
                return
            dfs(root.left, leaves)
            dfs(root.right, leaves)
        
        tree1 = []
        tree2 = []
        dfs(root1, tree1)
        dfs(root2, tree2)
        return tree1 == tree2