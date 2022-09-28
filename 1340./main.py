from queue import PriorityQueue

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        dp = [1] * len(arr)
        q = PriorityQueue()
        
        for i in range(len(arr)):
            q.put((arr[i], i))
            
        while not q.empty():
            current = q.get()
            index = current[1]
            lower_bound = max(0, index - d)
            upper_bound = min(len(arr), index + d + 1)
            current_max = dp[index]
            
            for j in range(index + 1, upper_bound):
                if arr[j] >= current[0]:
                    break
                current_max = max(dp[j] + 1, current_max)
                
            for j in range(index - 1, lower_bound - 1, -1):
                if arr[j] >= current[0]:
                    break
                current_max = max(dp[j] + 1, current_max)
                
            dp[index] = current_max
        
        result = 0
        for i in range(len(dp)):
            result =  max(dp[i], result)
            
        return result
