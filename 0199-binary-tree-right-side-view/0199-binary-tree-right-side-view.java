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
    private int maxLevel = 0;
    
    private void bfs(TreeNode root, int level, List<Integer> list) {
        if (root == null) {
            return ;
        }    
        if (level > maxLevel) {
            list.add(root.val);
            maxLevel = level;
        }
        bfs(root.right, level + 1, list);
        bfs(root.left, level + 1, list);
    }
    
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> right = new ArrayList<>();
        bfs(root, 1, right);
        return right;
    }
}