class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        times_appeared = 0
        element = 0
        n = 0
        while times_appeared <= len(nums) / 2 and n < len(nums):
            if element == nums[n]:
                times_appeared += 1
                n += 1
            else:
                times_appeared = 1
                element = nums[n]
                n += 1
        return element