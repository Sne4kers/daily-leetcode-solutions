import numpy as np

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = np.zeros((n+1, target+1),dtype=np.int)
        mod = 10**9 + 7
        
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            for j in range(1, target+1):
                dp[i][j] = sum(dp[i-1][max(j-k, 0):j]) % mod
        
        return dp[n][target]
