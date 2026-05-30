from typing import List
from bisect import bisect_left

class Fenwick:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def update(self, i, val):
        i += 1
        while i <= self.n:
            self.bit[i] = max(self.bit[i], val)
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i > 0:
            res = max(res, self.bit[i])
            i -= i & -i
        return res


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        mx = max(q[1] for q in queries)

        obstacles = {0, mx + 1}
        for q in queries:
            if q[0] == 1:
                obstacles.add(q[1])

        pos = sorted(obstacles)

        bit = Fenwick(mx + 2)

        for i in range(1, len(pos)):
            bit.update(pos[i], pos[i] - pos[i - 1])

        ans = []

        for q in reversed(queries):
            if q[0] == 2:
                _, x, sz = q

                idx = bisect_left(pos, x + 1)
                r = pos[idx]
                l = pos[idx - 1]

                best = bit.query(l)
                best = max(best, x - l)

                ans.append(best >= sz)

            else:
                _, x = q

                idx = bisect_left(pos, x)

                l = pos[idx - 1]
                r = pos[idx + 1]

                pos.pop(idx)

                bit.update(r, r - l)

        return ans[::-1]