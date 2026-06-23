class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int number = 0;
        int counter = 0;
        for(int i = 0; i < nums.size(); i++){
            number = nums[i];
            counter = 0;
            for(int j = 0; j < nums.size(); j++){
                if(number == nums[j]){
                counter++;
                }
            }
            if(counter > 1){
                return true;
            }
            
        }
        return false;
    }
};
