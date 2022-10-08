class Solution {
public:
    int search(vector<int>& nums, int target) {
        return binarySearch(nums, target, 0, nums.size() - 1);
    }
    
    int binarySearch(vector<int>& nums, int target, int begin, int end){
        int mid = (begin + end) / 2;
        while (begin != end) {
            mid = (begin + end) / 2;
            if (nums[mid] == target)
                return mid;
            if (nums[mid] > target)
                end = mid;
            else
                begin = mid + 1;
        }
        if (nums[begin] == target)
            return begin;
        else
            return -1;
    }
};
