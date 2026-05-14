class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=max(nums)
        if len(nums)!=n+1:
            return False
        count=Counter(nums)
        return all(count[i]==1 for i in range(1,n)) and count[n]==2  