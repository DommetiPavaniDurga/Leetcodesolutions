class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        total = sum(cardPoints)
        window_size = n - k
        
        # Initial window sum
        curr = sum(cardPoints[:window_size])
        min_sum = curr
        
        # Sliding window
        for i in range(window_size, n):
            curr += cardPoints[i] - cardPoints[i - window_size]
            min_sum = min(min_sum, curr)
        
        return total - min_sum
