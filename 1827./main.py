class Solution:
    def minOperations(self, nums: List[int]) -> int:
        result = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] <= prev:
                result += prev - nums[i] + 1
                prev += 1
            else:
                prev = nums[i]
        return result
