class Solution {
    public int longestOnes(int[] nums, int k) {
        int start = 0, end = 0, max = 0;
        int zcount = 0;
        
        while (end < nums.length) {
            if (nums[end] == 0) {
                zcount++;
            }
            while (zcount > k && start <= end) {
                if (nums[start++] == 0) {
                    zcount--;
                }
            }
            max = Math.max(end - start + 1, max);
            end++;
        }
        return max;
    }
}