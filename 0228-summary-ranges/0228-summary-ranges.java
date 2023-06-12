class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> range = new ArrayList<>();
        int i = 0;
        
        while (i < nums.length) {
            StringBuilder sb = new StringBuilder();
            sb.append(nums[i++]);
            while (i < nums.length && nums[i] - nums[i - 1] == 1) {
                i++;
            }
            if (Integer.parseInt(sb.toString()) != nums[i - 1]) {
                sb.append("->");
                sb.append(nums[i - 1]);
            }
            range.add(sb.toString());
        }
        return range;
    }
}