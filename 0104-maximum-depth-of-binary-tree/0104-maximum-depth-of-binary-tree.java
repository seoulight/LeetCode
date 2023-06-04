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
    
    public int dfs(TreeNode root, int depth) {
        int max = depth;
        if (root.left != null) {
            max = Math.max(dfs(root.left, depth + 1), max);
        } 
        if (root.right != null) {
            max = Math.max(dfs(root.right, depth + 1), max);
        }
        return max;
    }
    
    public int maxDepth(TreeNode root) {
        if (root == null) return 0;
        return dfs(root, 1);
    }
}