class Solution {
    public int pivotIndex(int[] nums) {
        int totalsum=0;
        for(int i=0;i<nums.length;i++){
            totalsum+=nums[i];
        }
        int leftsum=0;
        for(int i=0;i<nums.length;i++){
            int rightsum=totalsum-nums[i]-leftsum;
            if(leftsum == rightsum){
                return i;
            }
            leftsum+=nums[i];
        }
        return -1;    
    }
}