class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map=dict()
        for i in range(0,len(nums)):
            if nums[i] in freq_map:
                freq_map[nums[i]]+=1
            else:
                freq_map[nums[i]]=1
            n = len(nums)
            if freq_map[nums[i]] > n // 2:
                return nums[i]