class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int left = 1, right = getMax(piles), result = right;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (canFinish(piles, h, mid)) {
                result = mid;
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return result;
    }

    private static boolean canFinish(int[] piles, int h, int speed) {
        int hours = 0;
        for (int pile : piles) {
            hours += (pile + speed-0.5) / speed; 
        }
        return hours <= h;
    }

    private static int getMax(int[] piles) {
        int max = 0;
        for (int pile : piles) {
            max = Math.max(max, pile);
        }
        return max;
    }
        
}
