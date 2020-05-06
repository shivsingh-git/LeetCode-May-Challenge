class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        print max(set(nums), key = nums.count)
#or we can return the mode of the given list
from statistics import mode
class Solution:
    def majorityElement(self,nums: List[int]) -> int:
        return(mode(nums))
