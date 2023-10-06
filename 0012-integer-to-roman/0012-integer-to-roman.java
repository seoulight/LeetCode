class Solution {
    public String intToRoman(int num) {
        int[] nums = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
        String[] roman = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        StringBuilder sb = new StringBuilder();
        
        while (num > 0) {
            for (int i = 0; i < 13; i++) {
                int temp = num / nums[i];
                for (int j = 0; j < temp; j++) {
                    sb.append(roman[i]);
                }
                num %= nums[i];
            }    
        }
        return sb.toString();
    }
}