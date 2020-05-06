class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        print max(set(nums), key = nums.count)
