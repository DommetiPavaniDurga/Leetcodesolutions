class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        chset=set(nums)
        for num in chset:
            if  num-1 not in chset:
                curr=num
                currlength=1
                while curr+1 in chset:
                    currlength+=1
                    curr+=1
                longest=max(longest,currlength)
        return longest

        