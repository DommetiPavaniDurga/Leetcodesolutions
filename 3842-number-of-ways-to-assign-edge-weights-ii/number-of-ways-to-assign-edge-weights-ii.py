from typing import List
from collections import defaultdict, deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = len(edges) + 1

        g = defaultdict(list)
        for u, v in edges:
            u -= 1
            v -= 1
            g[u].append(v)
            g[v].append(u)

        LOG = n.bit_length()
        depth = [0] * n
        up = [[-1] * LOG for _ in range(n)]

        parent = [-1] * n
        parent[0] = 0

        q = deque([0])

        while q:
            u = q.popleft()
            for v in g[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)

        for i in range(n):
            up[i][0] = parent[i]

        for j in range(1, LOG):
            for i in range(n):
                up[i][j] = up[up[i][j - 1]][j - 1]

        def lca(a, b):
            if depth[a] < depth[b]:
                a, b = b, a

            diff = depth[a] - depth[b]

            for j in range(LOG):
                if diff & (1 << j):
                    a = up[a][j]

            if a == b:
                return a

            for j in range(LOG - 1, -1, -1):
                if up[a][j] != up[b][j]:
                    a = up[a][j]
                    b = up[b][j]

            return up[a][0]

        pow2 = [1] * (n + 1)
        for i in range(1, n + 1):
            pow2[i] = (pow2[i - 1] * 2) % MOD

        ans = []

        for u, v in queries:
            u -= 1
            v -= 1

            w = lca(u, v)
            dist = depth[u] + depth[v] - 2 * depth[w]

            if dist == 0:
                ans.append(0)
            else:
                ans.append(pow2[dist - 1])

        return ans