class Solution {
    public int longestSubarray(int[] nums) {
        int i = 0, j = 0, zcount = 0;
        int max = 0;
        
        while (j < nums.length) {
            if (nums[j] == 0) {
                zcount++;
            }
            while (zcount > 1 && i < j) {
                if (nums[i++] == 0) {
                    zcount--;
                }
            }
            max = Math.max(max, j - i);
            j++;
        }
        return max;
    }
}