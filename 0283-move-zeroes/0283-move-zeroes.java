class Solution {
    
    public void swap(int a, int b, int[] nums) {
        int temp = nums[a];
        nums[a] = nums[b];
        nums[b] = temp;
    }
    
    public void moveZeroes(int[] nums) {
        int size = 0;
        
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 0) {
                size++;
            }
            else if (size > 0) {
                int tmp = nums[i];
                nums[i] = 0;
                nums[i - size] = tmp;
            }
        }        
        
    }
}