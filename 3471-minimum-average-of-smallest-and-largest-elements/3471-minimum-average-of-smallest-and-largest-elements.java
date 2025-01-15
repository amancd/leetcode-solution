class Solution {
    public double minimumAverage(int[] nums) {
        Arrays.sort(nums);

        int left = 0;
        int right = nums.length - 1;
        ArrayList<Float> average = new ArrayList<>();

        while(left<right){
            average.add((nums[left] + nums[right])/2.0f);

            left+=1;
            right-=1;
        }

        float min = Collections.min(average);

        return min;
    }
}