class Solution {
    public boolean increasingTriplet(int[] nums) {
        if (nums.length < 3) {
            return false;
        }
        
        int max1 = Integer.MAX_VALUE, max2 = Integer.MAX_VALUE;
        
        for(int val : nums){
            if(val <= max1) max1 = val; 
            else if(val <= max2) max2 = val; 
            else return true; 
        }
        
        return false;
    }
}