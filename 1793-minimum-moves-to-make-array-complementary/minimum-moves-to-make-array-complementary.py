from typing import List

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diff = [0] * (2 * limit + 2)  # difference array

        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            low, high = min(a, b), max(a, b)

            # Default: 2 moves for all sums
            diff[2] += 2

            # Reduce to 1 move for sums in [low+1, high+limit]
            diff[low + 1] -= 1
            diff[high + limit + 1] += 1

            # Reduce to 0 moves for exact sum = a+b
            diff[a + b] -= 1
            diff[a + b + 1] += 1

        res = float("inf")
        curr = 0
        for s in range(2, 2 * limit + 1):
            curr += diff[s]
            res = min(res, curr)

        return res
