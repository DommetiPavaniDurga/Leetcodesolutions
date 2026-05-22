class Solution:
    def countOdds(self, low: int, high: int) -> int:
        total=high-low+1
        count=total//2
        if low%2==1 and high%2==1:
            count+=1
        return count