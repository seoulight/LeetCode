/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    
    private int zigzag(TreeNode root, int deepth, boolean direction) {
        if (root == null) {
            return deepth - 1;
        }
        if (direction) {
            return Math.max(zigzag(root.right, deepth + 1, false), zigzag(root.left, 1, true));
        } else {
            return Math.max(zigzag(root.left, deepth + 1, true), zigzag(root.right, 1, false));
        }
    }
    
    public int longestZigZag(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return Math.max(zigzag(root.left, 1, true), zigzag(root.right, 1, false));
    }
}