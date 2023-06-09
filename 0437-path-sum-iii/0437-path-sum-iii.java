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
    public int dfs(TreeNode root, Map<Long, Integer> prevSum, long currSum, int targetSum) {
        if (root == null) {
            return 0;
        }
        
        currSum += root.val;
        int res = prevSum.getOrDefault(currSum - targetSum, 0);
        prevSum.put(currSum, prevSum.getOrDefault(currSum, 0) + 1);
        
        res += dfs(root.left, prevSum, currSum, targetSum) + dfs(root.right, prevSum, currSum, targetSum);
        prevSum.put(currSum, prevSum.get(currSum) - 1);
        return res;
    }
    public int pathSum(TreeNode root, int targetSum) {
        Map<Long, Integer> prevSum = new HashMap<>();
        
        prevSum.put((long)0, 1);
        return dfs(root, prevSum, 0, targetSum);
    }
}