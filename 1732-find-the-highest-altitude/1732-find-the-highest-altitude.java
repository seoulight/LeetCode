class Solution {
    public int largestAltitude(int[] gain) {
        int max = 0, altitude = 0;
        
        for (int i = 0; i < gain.length; i++) {
            altitude += gain[i];
            max = Math.max(max, altitude);
        }
        return max;
    }
}