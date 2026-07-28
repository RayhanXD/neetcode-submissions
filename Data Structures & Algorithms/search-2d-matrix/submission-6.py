class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = len(matrix) - 1

        while (l <= r):

            middle = (l + r) // 2
            if target in matrix[middle]:
                return True
            elif target > matrix[middle][-1]:
                l = middle + 1
            else:
                r = middle - 1

        return False