import java.util.HashSet;
class Solution {
    public int repeatedNTimes(int[] nums) {
        HashSet<Integer> seen = new HashSet<Integer>();
        for(int i =0; i<=nums.length -1;i++){
            if(seen.contains(nums[i]))
                return nums[i];
            else{seen.add(nums[i]);}
        }
        return 0;
    }
}