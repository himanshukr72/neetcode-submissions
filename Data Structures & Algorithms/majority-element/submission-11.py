class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq_map={}
        for i in range(0, len(nums)):
            freq_map[nums[i]]=freq_map.get(nums[i],0)+1
        n = len(nums)
        for num in freq_map:
            if freq_map[num] > n // 2:
                return num