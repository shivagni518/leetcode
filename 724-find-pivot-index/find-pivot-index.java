class Solution {
    public int pivotIndex(int[] nums) {
        int totalsum=0;
        for(int i=0;i<nums.length;i++){
            totalsum+=nums[i];
        }
        int leftsum=0;
        for(int i=0;i<nums.length;i++){
            int current=nums[i];
            int rightsum=totalsum-current-leftsum;
            if(leftsum == rightsum){
                return i;
            }
            leftsum+=current;
        }
        return -1;    
    }
}