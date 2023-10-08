class Solution {
    public int maxDotProduct(int[] nums1, int[] nums2) {
        int len1 = nums1.length, len2 = nums2.length, dp[][] = new int[len1][len2];
        
        for (int i = 0; i < len1; i++) {
            for (int j = 0; j < len2; j++) {
                dp[i][j] = nums1[i] * nums2[j];
                if (i > 0 && j > 0) dp[i][j] += Math.max(dp[i - 1][j - 1], 0);
                if (i > 0) dp[i][j] = Math.max(dp[i - 1][j], dp[i][j]);
                if (j > 0) dp[i][j] = Math.max(dp[i][j - 1], dp[i][j]);
            }
        }
        return dp[len1 - 1][len2 - 1];
    }
}