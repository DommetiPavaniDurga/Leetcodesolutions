import heapq

class Solution:
    def maxTotalValue(self, nums, k):
        n = len(nums)

        # Precompute Sparse Tables for RMQ (max and min)
        import math
        log = [0] * (n + 1)
        for i in range(2, n + 1):
            log[i] = log[i // 2] + 1

        K = log[n] + 1
        st_max = [[0] * n for _ in range(K)]
        st_min = [[0] * n for _ in range(K)]

        for i in range(n):
            st_max[0][i] = nums[i]
            st_min[0][i] = nums[i]

        for j in range(1, K):
            for i in range(n - (1 << j) + 1):
                st_max[j][i] = max(st_max[j-1][i], st_max[j-1][i + (1 << (j-1))])
                st_min[j][i] = min(st_min[j-1][i], st_min[j-1][i + (1 << (j-1))])

        def query_max(l, r):
            j = log[r - l + 1]
            return max(st_max[j][l], st_max[j][r - (1 << j) + 1])

        def query_min(l, r):
            j = log[r - l + 1]
            return min(st_min[j][l], st_min[j][r - (1 << j) + 1])

        # Initialize heap with subarrays ending at n-1
        heap = []
        for l in range(n):
            val = query_max(l, n-1) - query_min(l, n-1)
            heapq.heappush(heap, (-val, l, n-1))  # max-heap via negative values

        total = 0
        for _ in range(k):
            val, l, r = heapq.heappop(heap)
            total += -val
            if r - 1 >= l:
                new_val = query_max(l, r-1) - query_min(l, r-1)
                heapq.heappush(heap, (-new_val, l, r-1))

        return total
