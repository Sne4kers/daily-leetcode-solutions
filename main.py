class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = 0
        slow = 0
        fast = nums[nums[fast]]
        slow = nums[slow]
        while fast != slow:
            fast = nums[nums[fast]]
            slow = nums[slow]
        slow = 0
        while nums[fast] != nums[slow]:
            slow = nums[slow]
            fast = nums[fast]
        return nums[slow]
