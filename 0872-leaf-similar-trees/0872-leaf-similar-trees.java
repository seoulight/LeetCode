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
    
    public void dfs(TreeNode root, List<Integer> leaf) {
        if (root == null)
            return ;
        if (root.left == null && root.right == null) {
            leaf.add(root.val);
            return ;
        }
        dfs(root.left, leaf);
        dfs(root.right, leaf);
    }
    
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> seq1 = new ArrayList<>();
        List<Integer> seq2 = new ArrayList<>();
        
        dfs(root1, seq1);
        dfs(root2, seq2);
        return seq1.equals(seq2);
    }
}