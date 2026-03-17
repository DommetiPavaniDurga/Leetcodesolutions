class Solution(object):
    def longestConsecutive(self, nums):
        if not nums:
            return 0
        nums.sort()
        longest=1
        curr=1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i]==nums[i-1]+1:
                curr+=1
                longest=max(longest,curr)
            else:
                curr=1
        return longest
        """
        :type nums: List[int]
        :rtype: int
        """
        