class Solution {
public:
    int countDigitOccurrences(vector<int>& nums, int digit) {
        int count =0;
        for(int num : nums){
            count += inNum(num,digit);
        }
        return count;
    }

    int inNum(int num, int digit){
        int count = 0;
        while(num){
            int temp = num % 10;
            num /= 10;
            if(temp == digit)
                count++; 
        }
        return count;
    }
};