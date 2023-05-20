class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int sum = 0, start = 0, end = 0;
        int max = Integer.MIN_VALUE;
        
        while (end < nums.length) {
            if (end - start < k) {
                sum += nums[end];
                end++;
            }
            if (end - start == k) {
                max = Math.max(max, sum);
                sum -= nums[start++];
            }
        }
        return (double)max / k;
    }
}