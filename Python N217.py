class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = 0
        while n < len(nums) - 1:
            if nums[n] == nums[n + 1]:
                return 0 == 0
            else:
                n += 1
        return 0 == 1