class Solution {
    public boolean isSubsequence(String s, String t) {
        int subIdx = 0;
        char[] charsS = s.toCharArray(), charsT = t.toCharArray();
        
        for (int i = 0; i < t.length() && subIdx < s.length(); i++) {
            if (charsS[subIdx] == charsT[i]) {
                subIdx++;
            }
        }
        return subIdx == s.length();        
    }
}