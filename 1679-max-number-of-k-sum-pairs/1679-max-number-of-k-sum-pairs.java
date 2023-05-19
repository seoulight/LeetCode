class Solution {
    public int maxOperations(int[] nums, int k) {
        int answer = 0, i = 0, j = nums.length - 1;
        
        Arrays.sort(nums);
        while (i < j) {
            if (nums[i] + nums[j] == k) {
                answer++;
                i++;
                j--;
            } else if (nums[i] + nums[j] < k) {
                i++;
            } else {
                j--;
            }
        }
        return answer;
    }
}