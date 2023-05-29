class RecentCounter {
    
    Deque<Integer> counter;

    public RecentCounter() {
        counter = new ArrayDeque<>();
    }
    
    public int ping(int t) {
        counter.add(t);
        for (Integer c : counter) {
            if (c < t - 3000) {
                counter.removeFirst();
            }
        }
        return counter.size();
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */