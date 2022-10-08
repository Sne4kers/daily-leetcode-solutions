class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        prev = -1
        flag = False
        for i in range(len(matrix)):
            if matrix[i][0] > target:
                flag = True
                break
            else:
                prev += 1
                
        if not flag:
            prev = -1
            
        for i in range(len(matrix[prev])):
            if matrix[prev][i] == target:
                return True
        return False
