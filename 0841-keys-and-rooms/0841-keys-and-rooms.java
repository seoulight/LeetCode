class Solution {
    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        boolean[] visited = new boolean[rooms.size()];
        Arrays.fill(visited, false);
        Queue<List<Integer>> q = new LinkedList<>();
        
        q.add(rooms.get(0));
        visited[0] = true;
        while (!q.isEmpty()) {
            List<Integer> nums = q.poll();
            for (int num : nums) {
                if (!visited[num]) {
                    visited[num] = true;
                    q.add(rooms.get(num));
                }
            }
        }
        for (boolean v : visited) {
            if (!v) {
                return false;   
            }
        }
        return true;
    }
}