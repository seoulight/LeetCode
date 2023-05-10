class Solution {
    
    public boolean isVowels(char c) {
        // return "aeiouAEIOU".contains(String.valueOf(c));
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
            || c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U';
    }
    
    public void swap(char[] chars, int x, int y) {
        char tmp = chars[x];
        chars[x] = chars[y];
        chars[y] = tmp;
    }
    
    public String reverseVowels(String s) {
        char[] answer = s.toCharArray();
        int start = 0, end = s.length() - 1;
        
        while (start < end) {
            while (start < s.length() && !isVowels(answer[start])) {
                start++;
            }
            while (end >= 0 && !isVowels(answer[end])) {
                end--;
            }
            if (start < end) {
                swap(answer, start++, end--);
            }
        }
        return new String(answer);
    }
}