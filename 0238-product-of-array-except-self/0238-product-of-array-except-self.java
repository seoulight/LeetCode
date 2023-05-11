class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] answer = new int[nums.length];
        int[] prefix = new int[nums.length];
        int[] suffix = new int[nums.length];
        
        prefix[0] = nums[0];
        suffix[nums.length - 1] = nums[nums.length - 1];
        for (int i = 1; i < nums.length; i++) {
            prefix[i] = prefix[i - 1] * nums[i];
            suffix[nums.length - i - 1] = suffix[nums.length - i] * nums[nums.length - i - 1];
        }
        
        for (int i = 0; i < nums.length; i++) {
            if (i == 0) {
                answer[i] = suffix[i + 1];
            }
            else if (i == nums.length - 1) {
                answer[i] = prefix[i - 1];
            }
            else {
               answer[i] = prefix[i - 1] * suffix[i + 1];  
            }
        }
        return answer;
    }
}