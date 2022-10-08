class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int begin = 0;
        int end = nums.size();
        while(end > begin){
            int mid = begin + (end - begin) / 2;
            if (nums[mid] == target)
                return mid;
            if (nums[mid] > target)
                end = mid;
            else
                begin = mid + 1;
        }
        return begin;
    }
};
