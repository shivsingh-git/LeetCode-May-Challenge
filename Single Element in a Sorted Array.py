#its a binary search approach
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1                                    #creating the required sets of prelimenry conditions(left is frst node right is the last node)
        while left < right:
            mid = int((left + right)/2)                                 #finding the mid term of the list
            if (mid % 2 == 1 and nums[mid - 1] == nums[mid]) or (mid%2 == 0 and nums[mid] == nums[mid + 1]):        #if the mid condition is satisfying the given set of sls
                left = mid + 1
            else:
                right = mid
        return nums[left]
