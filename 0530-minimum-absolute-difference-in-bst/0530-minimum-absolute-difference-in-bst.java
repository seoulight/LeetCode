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
    private int min = 100001;
    private int prev = -1;
    
    private void inorder(TreeNode root) {
        if (root == null) {
            return ;
        }
        inorder(root.left);
        if (prev > -1) {
            min = Math.min(Math.abs(prev - root.val), min);
        }
        prev = root.val;
        inorder(root.right);
    }
    
    public int getMinimumDifference(TreeNode root) {
        inorder(root);
        return min;
    }
}