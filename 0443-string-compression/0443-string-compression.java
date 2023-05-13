class Solution {
    public int compress(char[] chars) {
        int i = 0, totalLen = 0, nextIdx = 0;
        
        while (i < chars.length) {
            int cnt = 1;
            char c = chars[i++];
            
            while (i < chars.length && chars[i] == c) {
                i++;
                cnt++;
            }
            chars[nextIdx++] = c;
            totalLen++;
            if (cnt > 1) {
                for (char num : String.valueOf(cnt).toCharArray()) {
                    chars[nextIdx++] = num;
                    totalLen++;
                }
            }
        }
        return totalLen;
    }
}