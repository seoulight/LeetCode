class Solution {
    public boolean uniqueOccurrences(int[] arr) {
        Map<Integer, Integer> num_count = new HashMap<>();
        
        for (int num : arr) {
            if (!num_count.containsKey(num)) {
                num_count.put(num, 0);
            }
            num_count.put(num, num_count.get(num) + 1);
        }
        Set<Integer> counts = new HashSet<>();
        for (int key : num_count.keySet()) {
            int value = num_count.get(key);
            if (counts.contains(value)) {
                return false;
            }
            counts.add(value);
        }
        return true;
    }
}