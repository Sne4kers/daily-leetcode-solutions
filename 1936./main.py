class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        answer = 0
        previous = 0
        for i in range(len(rungs)):
            if rungs[i] - previous > dist:
                if (rungs[i] - previous) % dist == 0:
                    answer += (rungs[i] - previous) // dist - 1
                else:
                    answer += (rungs[i] - previous) // dist
            previous = rungs[i]
        return answer
