class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        if nums[l] > nums[r]:
            while l < r:
                mid = l + (r - l) // 2

                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid + 1

            pivot = l

            if nums[0] <= target <= nums[pivot - 1]:
                l, r = 0, pivot - 1
            else:
                l, r = pivot, len(nums) - 1
        
        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return -1