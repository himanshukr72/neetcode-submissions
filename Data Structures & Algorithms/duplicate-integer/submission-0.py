class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasset = set()
        if len(nums) != len(set(nums)):
            return True
        else:
            return False