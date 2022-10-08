class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seenNumbers;
        vector<int> result(2);
        for(int i = 0; i < nums.size(); i++) {
            if(seenNumbers.find(target - nums[i]) != seenNumbers.end()) {
                result[0] = i;
                result[1] = seenNumbers[target - nums[i]];
                return result;
            }
            seenNumbers[nums[i]] = i;
        }
        return result;
    }
};
