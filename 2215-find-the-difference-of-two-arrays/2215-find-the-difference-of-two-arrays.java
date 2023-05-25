class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        List<List<Integer>> answer = new ArrayList<>();
        
        for (int i = 0; i < nums1.length; i++) {
            set1.add(nums1[i]);
        }
        for (int i = 0; i < nums2.length; i++) {
            set2.add(nums2[i]);
        }
        Iterator<Integer> it = set1.iterator();
        answer.add(new ArrayList<>());
        while (it.hasNext()) {
            int n = it.next();
            if (!set2.contains(n)) { 
                answer.get(0).add(n);
            }
        }
        it = set2.iterator();
        answer.add(new ArrayList<>());
        while (it.hasNext()) {
            int n = it.next();
            if (!set1.contains(n)) {
                answer.get(1).add(n);
            }
        }
        return answer;
    }
}