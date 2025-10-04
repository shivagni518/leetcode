class Solution {
    public boolean isHappy(int n) {
        HashSet <Integer> seen = new HashSet<>();
        while(n != 1 && !seen.contains(n)){
            seen.add(n);
            n = getNxt(n);
        }
        return n == 1;   
    }
    private static int getNxt(int n){
        int sum = 0;
        while(n > 0){
            int digit = n%10;
            sum += digit*digit;
            n /= 10;
        }
        return sum;
    }
}