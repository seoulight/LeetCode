class Solution {
    public String reverseWords(String s) {
        int start = s.length() - 1, end = s.length() - 1;
        StringBuilder sb = new StringBuilder();
        
        
        while (start >= 0) {
            while (end > 0 && s.charAt(end) == ' ') {
                start--;
                end--;
            }
            while (start > 0 && s.charAt(start - 1) != ' ') {
                start--;
            }
            if (s.charAt(start) != ' ') {
                if (sb.length() > 0) {
                    sb.append(" ");
                }
                sb.append(s.substring(start, end + 1));
            }
            end = --start;
        }
        return sb.toString();
    }
}