from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        node_to_level = defaultdict(list)
        def checkValue(node: Optional[TreeNode], level: int):
            if level % 2 == 0 and (node.val % 2 == 0 or (node_to_level[level] and node_to_level[level][-1] >= node.val)):
                return False
            if level % 2 > 0 and (node.val % 2 > 0 or (node_to_level[level] and node_to_level[level][-1] <= node.val)):
                return False
            return True
        
        def checkLevel(root: Optional[TreeNode]) -> bool:
            q = deque([(root, 0)])
            while q:
                node, level = q.popleft()
                if not checkValue(node, level):
                    return False
                node_to_level[level].append(node.val)
                if node.left:
                    q.append((node.left, level + 1))
                if node.right:
                    q.append((node.right, level + 1))
            return True
        
        return checkLevel(root)
                