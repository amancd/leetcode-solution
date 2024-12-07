class Solution {
    public int minimumSize(int[] nums, int maxOperations) {
        int right = Arrays.stream(nums).max().getAsInt();
        int left = 1;
        
        while(left<right){
            int mid = (left + right)/2;
            int total = 0;
            for (int num : nums) {
                total += (num - 1) / mid;
            }

            if(total<=maxOperations){
                right = mid;
            }
            else{
                left = mid + 1;
            }
        
        }

        return left;
    }
}