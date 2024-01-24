# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        answer = 0
        def is_palindromic(digit_count: dict):
            odd = False
            for count in digit_count.values():
                if count % 2 > 0 and not odd:
                    odd = True
                elif count % 2 > 0 and odd:
                    return False
            return True
        
        def dfs(digit_count: dict, curr: Optional[TreeNode]):
            if not curr.left and not curr.right and is_palindromic(digit_count):
                nonlocal answer
                answer += 1
            if curr.left:
                digit_count[curr.left.val] += 1
                dfs(digit_count, curr.left)
                digit_count[curr.left.val] -= 1
            if curr.right:
                digit_count[curr.right.val] += 1
                dfs(digit_count, curr.right)
                digit_count[curr.right.val] -= 1
        
        digit_count = defaultdict(int)
        digit_count[root.val] = 1
        dfs(digit_count, root)
        return answer