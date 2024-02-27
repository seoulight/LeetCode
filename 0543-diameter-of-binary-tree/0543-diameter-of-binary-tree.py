# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        class DiameterData:
            def __init__(self, diameter, height):
                self.diameter = diameter
                self.height = height
        
        def calculateDiameterAndHeight(root: Optional[TreeNode]) -> DiameterData:
            if not root:
                return DiameterData(0, 0)
            
            left_data = calculateDiameterAndHeight(root.left)
            right_data = calculateDiameterAndHeight(root.right)
            
            current_diameter = max(left_data.height + right_data.height, max(left_data.diameter, right_data.diameter))
            current_height = max(left_data.height, right_data.height) + 1
            return DiameterData(current_diameter, current_height)
        
        data = calculateDiameterAndHeight(root)
        return data.diameter