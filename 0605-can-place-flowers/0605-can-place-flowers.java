class Solution {
        
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        
        for (int i = 0; i < flowerbed.length && n > 0; i++) {
            boolean rightIsEmpty = (i == flowerbed.length - 1) || (flowerbed[i + 1] == 0);
            boolean leftIsEmpty = (i == 0) || (flowerbed[i - 1] == 0);
            
            if (flowerbed[i] == 0 && rightIsEmpty && leftIsEmpty) {
                flowerbed[i] = 1;
                n--;
            }
        }
        
        return n == 0;
    }
}