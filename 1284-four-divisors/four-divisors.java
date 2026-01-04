class Solution {
    public int sumFourDivisors(int[] nums) {
        int count =0;
        int sum =0;
        int temp =0;
        for(int i = 0;i <= nums.length -1;i++){
            for(int j = 2;j < nums[i];j++){
                if(count>2)
                    break;
                if(nums[i] % j ==0){
                    count++;
                    temp += j;
                }
            }
            if(count == 2)
                sum += temp +1+ nums[i];
            temp=0;
            count =0;
        }
        return sum;
    }
}