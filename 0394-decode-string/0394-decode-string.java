class Solution {
    public String decodeString(String s) {
        String curr = "";
        Stack<Integer> counts = new Stack<>();
        Stack<String> prev = new Stack<>();
        
        for (int i = 0; i < s.length(); i++) {
            if (Character.isDigit(s.charAt(i))) {
                int count = 0;
                while (Character.isDigit(s.charAt(i))) {
                    count = count * 10 + s.charAt(i++) - '0';
                }
                counts.push(count);
            } 
            if (s.charAt(i) == '[') {
                prev.push(curr);
                curr = "";
            } else if (s.charAt(i) == ']') {
                StringBuilder encoded = new StringBuilder(prev.pop());
                int count = counts.pop();
                for (int j = 0; j < count; j++) {
                    encoded.append(curr);
                }
                curr = encoded.toString();
            } else {
                curr += s.charAt(i);
            }
        }
        return curr;
    }
}