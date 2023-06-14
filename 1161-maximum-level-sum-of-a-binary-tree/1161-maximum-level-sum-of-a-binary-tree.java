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
    
    public int maxLevelSum(TreeNode root) {
        if (root.left == null && root.right == null) {
            return 1;
        }
        Queue<TreeNode> q = new LinkedList<>();
        int maxLevel = 0, maxSum = Integer.MIN_VALUE, level = 0;
        
        q.add(root);
        while (!q.isEmpty()) {
            int sum = 0, size = q.size();
            for (int i = 0; i < size; i++) {
                TreeNode curr = q.poll();
                sum += curr.val;
                if (curr.left != null) {
                    q.add(curr.left);
                }
                if (curr.right != null) {
                    q.add(curr.right);
                }
            }
            level++;
            if (sum > maxSum) {
                maxSum = sum;
                maxLevel = level;
            }
        }
        return maxLevel;
    }
}