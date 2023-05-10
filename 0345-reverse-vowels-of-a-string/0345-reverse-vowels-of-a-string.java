class Solution {
    
    public boolean isVowels(char c) {
        return "aeiouAEIOU".contains(String.valueOf(c));
    }
    
    public String reverseVowels(String s) {
        StringBuilder answer = new StringBuilder(s);
        int i = 0, j = answer.length() - 1;
        
        while (i < j) {
            while (i < s.length() && !isVowels(answer.charAt(i))) {
                i++;
            }
            while (j >= 0 && !isVowels(answer.charAt(j))) {
                j--;
            }
            if (i < j) {
                answer.setCharAt(i, s.charAt(j));
                answer.setCharAt(j--, s.charAt(i++));
            }
        }
        return answer.toString();
    }
}