from collections import defaultdict, deque
from math import isqrt

class Solution:
    def minJumps(self, nums):
        n = len(nums)
        if n == 1:
            return 0

        MAXV = max(nums) + 1

        # Smallest Prime Factor (SPF) sieve
        spf = list(range(MAXV))

        for i in range(2, isqrt(MAXV) + 1):
            if spf[i] == i:
                for j in range(i * i, MAXV, i):
                    if spf[j] == j:
                        spf[j] = i

        def is_prime(x):
            return x >= 2 and spf[x] == x

        # prime -> indices divisible by prime
        divisible = defaultdict(list)

        for i, x in enumerate(nums):
            temp = x
            factors = set()

            while temp > 1:
                p = spf[temp]
                factors.add(p)

                while temp % p == 0:
                    temp //= p

            for p in factors:
                divisible[p].append(i)

        # BFS
        dist = [-1] * n
        dist[0] = 0

        q = deque([0])
        used_prime = set()

        while q:
            i = q.popleft()
            d = dist[i]

            if i == n - 1:
                return d

            # adjacent moves
            if i - 1 >= 0 and dist[i - 1] == -1:
                dist[i - 1] = d + 1
                q.append(i - 1)

            if i + 1 < n and dist[i + 1] == -1:
                dist[i + 1] = d + 1
                q.append(i + 1)

            # teleport using prime value
            val = nums[i]

            if is_prime(val) and val not in used_prime:
                used_prime.add(val)

                for nxt in divisible[val]:
                    if dist[nxt] == -1:
                        dist[nxt] = d + 1
                        q.append(nxt)

        return -1