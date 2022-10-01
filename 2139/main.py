class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        operations = 0
        while target != 1 and maxDoubles > 0:
            if target % 2 == 1:
                operations += 1
            target = target // 2
            maxDoubles -= 1
            operations += 1
        operations += target - 1
        return operations
