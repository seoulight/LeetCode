class Solution {
    public boolean isSubsequence(String s, String t) {
        int subIdx = 0;
        
        for (int i = 0; i < t.length() && subIdx < s.length(); i++) {
            if (s.charAt(subIdx) == t.charAt(i)) {
                subIdx++;
            }
        }
        return subIdx == s.length();        
    }
}