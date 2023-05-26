class Solution {
    public boolean closeStrings(String word1, String word2) {
        if (word1.length() != word2.length()) {
            return false;
        }
        
        Map<Character, Integer> map1 = new HashMap<>();
        Map<Character, Integer> map2 = new HashMap<>();
        
        for (char w : word1.toCharArray()) {
            if (!map1.containsKey(w)) {
                map1.put(w, 0);
            }
            map1.put(w, map1.get(w) + 1);
        }
        for (char w : word2.toCharArray()) {
            if (!map2.containsKey(w)) {
                map2.put(w, 0);
            }
            map2.put(w, map2.get(w) + 1);
        }
        List<Integer> values1 = new ArrayList<>(map1.values());
        List<Integer> values2 = new ArrayList<>(map2.values());
        
        Collections.sort(values1);
        Collections.sort(values2);
        
        if (!values1.equals(values2)) {
            return false;
        }
        if (!map1.keySet().equals(map2.keySet())) {
            return false;
        }
        return true;
    }
}