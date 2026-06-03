from bisect import bisect_right
from math import inf

class Solution:
    def earliestFinishTime(
        self,
        landStartTime,
        landDuration,
        waterStartTime,
        waterDuration,
    ):
        def solve(Astart, Adur, Bstart, Bdur):
            rides = sorted(zip(Bstart, Bdur))
            starts = [s for s, d in rides]
            durs = [d for s, d in rides]

            n = len(rides)

            prefix = [inf] * n
            prefix[0] = durs[0]
            for i in range(1, n):
                prefix[i] = min(prefix[i - 1], durs[i])

            suffix = [inf] * n
            suffix[-1] = starts[-1] + durs[-1]
            for i in range(n - 2, -1, -1):
                suffix[i] = min(
                    suffix[i + 1],
                    starts[i] + durs[i]
                )

            ans = inf

            for s, d in zip(Astart, Adur):
                finishA = s + d

                idx = bisect_right(starts, finishA)

                if idx > 0:
                    ans = min(ans, finishA + prefix[idx - 1])

                if idx < n:
                    ans = min(ans, suffix[idx])

            return ans

        return min(
            solve(landStartTime, landDuration,
                  waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration,
                  landStartTime, landDuration)
        )