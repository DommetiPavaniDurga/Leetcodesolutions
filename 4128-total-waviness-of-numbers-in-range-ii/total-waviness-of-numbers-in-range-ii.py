from functools import cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def calc(n):
            if n < 0:
                return 0

            s = str(n)

            @cache
            def dfs(pos, tight, started, p1, p2):
                if pos == len(s):
                    return (1, 0)

                limit = int(s[pos]) if tight else 9
                cnt = 0
                wav = 0

                for d in range(limit + 1):
                    nt = tight and d == limit

                    if not started and d == 0:
                        c, w = dfs(pos + 1, nt, False, -1, -1)
                    elif not started:
                        c, w = dfs(pos + 1, nt, True, d, -1)
                    else:
                        add = 0
                        if p2 != -1:
                            if (p2 < p1 > d) or (p2 > p1 < d):
                                add = 1

                        c, w = dfs(pos + 1, nt, True, d, p1)
                        w += add * c

                    cnt += c
                    wav += w

                return cnt, wav

            return dfs(0, True, False, -1, -1)[1]

        return calc(num2) - calc(num1 - 1)