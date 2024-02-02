class Solution:
    def numWays(self, n: int, k: int) -> int:
        @cache
        def dfs(i):
            if i == n: return 1
            if i > n: return 0
            res = dfs(i+1) * (k-1) + dfs(i+2) * (k-1)
            return res
        res = (dfs(1) * k) + (dfs(2) * k)
        return res