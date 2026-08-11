class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                break
            if target <= matrix[mid][0]:
                r = mid - 1
            else:
                l = mid + 1


        row = matrix[mid]
        l, r = 0, len(row) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if target == row[mid]:
                return True
            if target <= row[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return False