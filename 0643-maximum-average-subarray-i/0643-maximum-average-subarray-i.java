class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int sum=0;
        for(int i=0;i<k;i++){
            sum+=nums[i];
        }
        int maxsum=sum;
        for(int i=k;i<nums.length;i++){
            sum=sum-nums[i-k]+nums[i];         
             //Jo adhicha sum ahe tyatun jo baher kadlay to (mhnjech pahila) substract karaycha ani jo ata add kelay(navin element) to add karaycha
            maxsum=Math.max(maxsum,sum);
        }
        return (double)maxsum/k;
    }
}