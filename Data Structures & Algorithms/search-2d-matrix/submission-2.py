class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_i = -1

        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                row_i = mid
                break
            elif target < matrix[mid][0]:
                r = mid - 1
            elif target > matrix[mid][-1]:
                l = mid + 1
    
        if row_i == -1:
            return False
        
        row = matrix[row_i]
        l, r = 0, len(row) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target == row[mid]:
                return True
            elif target < row[mid]:
                r = mid - 1
            elif target > row[mid]:
                l = mid + 1
        
        return False